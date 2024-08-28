# Notifications

## Sent toast notification

!!! question "Send toast notification"

    Show a toast notification in SeaTable's web interface to a user.

    ```python
    base.send_toast_notification(username, msg, toast_type='success')
    # toast_type: one of "success", "warning" or "danger"
    ```

    __Example__

    ```python
    base.send_toast_notification(
    "aea9e807bcfd4f3481d60294df74f6ee@auth.local",
    "error request",
    "danger"
    )
    ```
