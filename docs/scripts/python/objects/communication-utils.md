# Communication utility functions

Several outgoing communications features are available within SeaTable. Wether you want to communicate with a user in the web interface or or be alerted of database changes from another process, here are the methods you can use while scripting.


!!! info "Going further"
    Keep in mind that communication methods will probably require other coding skills as they mostly make sense outside of SeaTable. The [API Reference](https://api.seatable.com/reference/getbaseactivitylog-1) also details other methods such as getting base or row activities logs, which might also help you stay informed about what's happening in the base (but without the automatic firing on the SeaTable side of the methods presented here).

## Toast notifications

!!! abstract "send_toast_notification"

    Show a toast notification in SeaTable's web interface to a user. The username you have to provide is a unique identifier ending by `@auth.local`. This is **neither** the email address of the user **nor** its name. The content of `msg` is plain text.

    ```python
    base.send_toast_notification(username, msg, toast_type='success') # (1)!
    ```

    1. `toast_type` can be one of `success`, `warning` or `danger`

    __Example__

    ```python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    base.send_toast_notification(
    "aea9e807bcfd4f3481d60294df74f6ee@auth.local",
    "error request",
    "danger"
    )
    ```

    ```python
    from seatable_api import Base, context

    base = Base(context.api_token, context.server_url)
    base.auth()
    # Time to cheer up yourself!
    my_username = context.current_username
    base.send_toast_notification(
        my_username,
        "You're doing great!",
        "success"
    )
    ```

## Websockets

!!! abstract "socketIO"

    By using websocket, you can get __realtime data update notifications__ of a base.

    !!! info "websocket-client library recommended"

        You might encounter the warning `websocket-client package not installed, only polling transport is available` when you run the script below. The library is not required as you'll get the update infos anyway (using polling transport), but installing the websocket-client library will allow you to benefit from a real websocket transport.

    ```python
    from seatable_api import Base

    server_url = 'https://cloud.seatable.io'
    api_token = 'c3c75dca2c369849455a39f4436147639cf02b2d'

    base = Base(api_token, server_url)
    base.auth(with_socket_io=True) # (1)!

    base.socketIO.wait()
    ```

    1. Note that using websocket needs to specify the argument `with_socket_io=True` as compared to usual authentication

    When the base data is updated, the following will be output in the terminal.

    ```log
    2022-07-19 11:48:37.803956 [ SeaTable SocketIO connection established ]
    2022-07-19 11:48:39.953150 [ SeaTable SocketIO on UPDATE_DTABLE ]
    {"op_type":"insert_row","table_id":"0000","row_id":"YFK9bD1XReSuQ7WP1YYjMA","row_insert_position":"insert_below","row_data":{"_id":"RngJuRa0SMGXyiA-SHDiAw","_participants":[],"_creator":"seatable@seatable.com","_ctime":"","_last_modifier":"seatable@seatable.com","_mtime":""},"links_data":{}}
    ```

    After getting data update notifications, perform self-defined actions by listen to a specific event. Available events are `UPDATE_DTABLE` (database update) or `NEW_NOTIFICATION` (new notification received). Please note that we are here talking about SeaTable system's notifications (see the [User manual](https://seatable.com/help/homepage/notifications/) and not about the toast notifications fired by the `base.send_toast_notification` method).

    ```python
    import json
    from seatable_api import Base
    from seatable_api.constants import UPDATE_DTABLE # (1)!

    server_url = 'https://cloud.seatable.io'
    api_token = 'c3c75dca2c369849455a39f4436147639cf02b2d'

    def on_update(data, index, *args):
        try:
            operation = json.loads(data)
            print(operation)
            op_type = operation['op_type']
            table_id = operation['table_id']
            row_id = operation['row_id']
            # ... do something
        except Exception as e:
            print(e)

    base = Base(api_token, server_url)
    base.auth(with_socket_io=True)

    base.socketIO.on(UPDATE_DTABLE, on_update) # (2)!
    base.socketIO.wait()
    ```

    1. Note that you'll have to import the corresponding event (`UPDATE_DTABLE` or `NEW_NOTIFICATION`)

    2. First argument is the event triggering the system, second argument is the event handler (the name of the function that will be run when a new event happens)

## Webhooks

Another communication feature offered by SeaTable is Webhooks. Webhooks are covered in the [User manual](https://seatable.com/help/integrations/webhooks/) for global understanding and in the [API Reference](https://api.seatable.com/reference/listwebhooks) for webhook handlings functions. 

As SeaTable usually sends a webhook for every change, this might not be fully adapted if you need to track only a few changes. If you want to track only few operations (to trigger a workflow automation process for example), you can create [automation rules](https://seatable.com/help/automations-overview-seatable/) to send, via a Python script, a `POST` request to an incoming webhook, passing, for example, a string to identify the action and the id of the triggering row.

!!! warning "Enterprise subscription needed"

    Automations are available only with an [Enterprise subscription](https://seatable.com/help/subscription-plans/#seatable-cloud-enterprise-search).

__Example__

In this example, we can imagine setting up a simple automation rule triggered by a record update in a specific column that should trigger an automation process through a webhook. This automation will have a single "Run Python script" action launching the following script.

```python
import requests
from seatable_api import context

url = 'https://mywebhookurl.com'
data = {'action': 'transfer', '_id': context.current_row['_id']} # (1)!
try:
    response = requests.post(url, json = data)
    if response.status_code != 200:
        print('Failed request, status code: ', response.status_code)
        exit(1)
except Exception as e:
    print(e)
    exit(1)
print(response.text) # (2)!
```

1. You can actually pass whatever data you want in the `data` object. Here, there are two keys:
    - `action`: a string parameter allowing to switch processes depending on this parameter to allow one single entry point for several scenarios
    - `_id`: we pass the id of the triggering row to be able to use it on the webhook receiver side

2. Allows you to check if your request was successful or not