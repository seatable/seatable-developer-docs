# SeaTable\Client\AutomationsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createAutomationRule()**](AutomationsApi.md#createAutomationRule) | **POST** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/automation-rules/ | Create Automation Rule |
| [**deleteAutomationRule()**](AutomationsApi.md#deleteAutomationRule) | **DELETE** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/automation-rules/{automation_rule_id}/ | Delete Automation Rule |
| [**listAutomationRules()**](AutomationsApi.md#listAutomationRules) | **GET** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/automation-rules/ | List Automation Rules |
| [**updateAutomationRule()**](AutomationsApi.md#updateAutomationRule) | **PUT** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/automation-rules/{automation_rule_id}/ | Update Automation Rule |


## `createAutomationRule()`

```php
createAutomationRule($workspace_id, $base_name, $create_automation_rule_request): object
```

Create Automation Rule

You can set the automation rule to trigger by condition, or periodically. The following instruction shows you how to send the request body. Consult the example request for demonstration.  After successful creation, an `id` is returned, this is the ID of the automation rule you just created, and is to be distinguished from the action's `_id` like explained below in the actions section.  # First, define the running condition  For the `run_condition` parameter, use  - `per_update` for conditional trigger, if the rule should be triggered when a certain condition is met when the table has been updated; - `per_day`, `per_week`, or `per_month` for periodical trigger, if the rule should be triggered periodically.       # Then, define the trigger condition  In the `trigger` object, all the following params are required:  - `rule_name` is the name of this rule; - `table_id` is the ID of the table; - `view_id` is the ID of the view; - `condition` is how you'd like the rule to trigger. Use `filters_satisfy` for conditional trigger or `run_periodically` for periodical trigger.       ## Determine the trigger scenario if `run_condition` is `per_update`  In the automation rule's trigger conditions, you can watch some or all of the columns for changes, and eventually set filter conditions to narrow down the watching. So that means there are three typical scenarios:  - ### Watch all the columns without filters                 This is the simplest scenario: whenever a record has been changed, this rule will trigger. To do this, just define `watch_all_columns` as `true` and you are good to go:       ```     \"trigger\": {         \"rule_name\": \"Watch all\",         \"table_id\": \"0000\",         \"view_id\": \"0000\",         \"condition\": \"filters_satisfy\",         \"watch_all_columns\": true     }  ```  - ### Watch one or more columns without filters                 In the `column_keys` array, list the `key`s of columns you'd like to watch. Remember to set `watch_all_columns` to `false` (if you leave it as `true`, all the columns will be watched):       ```     \"trigger\": {         \"rule_name\": \"Watch Name and Select\",         \"table_id\": \"0000\",         \"view_id\": \"0000\",         \"condition\": \"filters_satisfy\",         \"column_keys\": [\"0000\", \"72IC\"]     }  ```  - ### To apply filters to the above scenarios                 You'll need two further params, if you'd like to filter the watched columns: - `filters` as an object. For details, refer to the **SeaTable API Parameter Reference** under \"filters\". - `filter_conjunction`: Use `And` or `Or` for the filter conjunction logic.       Here's an example:  ```     \"trigger\": {         \"rule_name\": \"test-auto\",         \"table_id\": \"0000\",         \"view_id\": \"0000\",         \"condition\": \"filters_satisfy\",         \"filters\": [{             \"column_key\": \"0000\",             \"filter_predicate\": \"contains\",             \"filter_term\": \"yes\"         }, {             \"column_key\": \"_creator\",             \"filter_predicate\": \"contains\",             \"filter_term\": [\"0027d98c471a4ee69eaf073508fc0d27@auth.local\"]         }],         \"filter_conjunction\": \"And\"     }  ```  ## Determine the trigger scenario if `run_condition` is `per_day`, `per_week`, or `per_month`  One or more further params are required:  - If the `run_condition` is `per_day`, define `notify_hour` here. Use `0` to `23` for the time of day you'd like the rule to trigger. - If the `run_condition` is `per_week`, define these two params:     - `notify_week_day`: Use an integer from `1` to `7` for Monday to Sunday, and     - `notify_week_hour`: Use `0` to `23` for the time of day you'd like the rule to trigger. - If the `run_condition` is `per_month`, define these two params:     - `notify_month_day`: Use an integer from `1` to `31` for the day of month. Attention: If it's set to `31` but a month doesn't have a 31st day, this rule won't be triggered. It'll only be triggered when the current day is a 31st.     - `notify_month_hour`: Use `0` to `23` for the time of day you'd like the rule to trigger.  See the example request for demonstration.  # Last but not least: The action  Different than the `trigger` object, the `actions` is a list of objects. This enables you to trigger multiple actions all at once.  **In each action object**, the `_id` is the first parameter. It's an ID of the action. If you have multiple actions in one rule, they should carry different IDs. You can decide which ID an action should carry.  ### To notify one or more users:  - `type` should be `notify`; - `users` is a list of user's IDs, it's optional if the `users_column_key` is defined; - `users_column_key` is a list of `key`s of columns that are the types of collaborator, creator or modifier; - `default_msg`: is the content of the message. You can use {column name} in the message to quote the content of a certain cell.       Example:  ```     \"actions\": [         {             \"type\": \"notify\",             \"users\": [],             \"default_msg\": \"look at {Name}.\",             \"_id\": \"740077\",             \"users_column_key\": \"iXRK\"         }     ]  ```  ### To modify the record:  - `type` should be `update_record`; - `updates` is an object including the column `key` and desired content of each field that you would like to modify.       Example:  ```     \"actions\": [         {             \"type\": \"update_record\",             \"updates\": {                 \"0000\": \"abc\",                 \"6NKm\": 123             },             \"_id\": \"54696\"         }     ]  ```  ### To lock the record:  - `type` should be `lock_record`; - `is_locked` set to `true` and the record that triggered the action will be locked.       Example:  ```     \"actions\": [         {             \"type\": \"lock_record\",             \"is_locked\": true,             \"_id\": \"872510\"         }     ]  ```  ### To add a new record:  - `type` should be `add_record`; - `row` is an object including the column `key` and desired content of each field that you would like to add in the new record.       Example:  ```     \"actions\": [         {             \"type\": \"add_record\",             \"row\": {                 \"0000\": \"abc\"             },             \"_id\": \"410993\"         }     ]  ```  ### To send an email:  - `type` should be `send_email`; - `account_id` is the ID of the third party account you added in this base. Refer to [Third Party Email Accounts](/reference/third-party-email-accounts) for details; - `send_to` is the receiver's email address. If you would like to send to multiple receivers, separate their email addresses with comma (,) inside of the quotation mark. - `copy_to` is the CC receiver's email address. For multiple addresses see above. - `subject` is the subject of your email. - `default_msg` is the content of the message.       Example:  ```     \"actions\": [         {             \"type\": \"send_email\",             \"default_msg\": \"Content example.\",             \"account_id\": 17,             \"subject\": \"Subject sample\",             \"send_to\": \"email@example.com, email2@example.com\",             \"copy_to\": \"email3@example.com, email4@example.com\",             \"_id\": \"838356\"         }     ] }  ```

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\AutomationsApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$create_automation_rule_request = new \SeaTable\Client\User\CreateAutomationRuleRequest(); // \SeaTable\Client\User\CreateAutomationRuleRequest

try {
    $result = $apiInstance->createAutomationRule($workspace_id, $base_name, $create_automation_rule_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AutomationsApi->createAutomationRule: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **create_automation_rule_request** | [**\SeaTable\Client\User\CreateAutomationRuleRequest**](../Model/CreateAutomationRuleRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deleteAutomationRule()`

```php
deleteAutomationRule($workspace_id, $base_name, $automation_rule_id): object
```

Delete Automation Rule

Delete an existing automation rule. This operation cannot be undone!

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\AutomationsApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$automation_rule_id = 20; // int

try {
    $result = $apiInstance->deleteAutomationRule($workspace_id, $base_name, $automation_rule_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AutomationsApi->deleteAutomationRule: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **automation_rule_id** | **int**|  | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listAutomationRules()`

```php
listAutomationRules($workspace_id, $base_name): object
```

List Automation Rules

List all the automation rules in a base.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\AutomationsApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.

try {
    $result = $apiInstance->listAutomationRules($workspace_id, $base_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AutomationsApi->listAutomationRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateAutomationRule()`

```php
updateAutomationRule($workspace_id, $base_name, $automation_rule_id, $create_automation_rule_request): object
```

Update Automation Rule

Update a base automation rule with this API request. Use the `id` you retrieved by listing automation rules or creating an automation rule.  For the exact parameters in the request body, consult the call \"Create A Base Automation Rule\".

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\AutomationsApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$automation_rule_id = 20; // int
$create_automation_rule_request = new \SeaTable\Client\User\CreateAutomationRuleRequest(); // \SeaTable\Client\User\CreateAutomationRuleRequest

try {
    $result = $apiInstance->updateAutomationRule($workspace_id, $base_name, $automation_rule_id, $create_automation_rule_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AutomationsApi->updateAutomationRule: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **automation_rule_id** | **int**|  | |
| **create_automation_rule_request** | [**\SeaTable\Client\User\CreateAutomationRuleRequest**](../Model/CreateAutomationRuleRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth



