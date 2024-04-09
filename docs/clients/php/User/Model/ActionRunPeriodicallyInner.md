# # ActionRunPeriodicallyInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **string** |  | [optional]
**users** | **string[]** |  | [optional]
**default_msg** | **string** | Is the content of the message. | [optional]
**_id** | **string** | It&#39;s an ID of the action.  If you have multiple actions in one rule, they should carry different IDs.  You can decide which ID an action should carry. | [optional]
**users_column_key** | **string** | Is a list of keys of columns that are the types of collaborator, creator or modifier. | [optional]
**account_id** | **int** | Is the ID of the third party account you added in this base. | [optional]
**subject** | **string** |  | [optional]
**send_to** | **string** | is the receiver&#39;s email address. For multiple addresses see above. | [optional]
**copy_to** | **string** | is the CC receiver&#39;s email address. For multiple addresses see above. | [optional]
**row** | **array<string,string>** | Is an object including the column key and desired content of each field that you would like to add in the new record. | [optional]
**link_id** | **string** |  | [optional]
**linked_table_id** | **string** |  | [optional]
**match_conditions** | [**\SeaTable\Client\User\ActionLinkRecordMatchConditionsInner[]**](ActionLinkRecordMatchConditionsInner.md) |  | [optional]
**script_name** | **string** |  | [optional]
**workspace_id** | **int** |  | [optional]
**owner** | **string** |  | [optional]
**org_id** | **int** |  | [optional]
**repo_id** | **string** |  | [optional]
**result_column** | **string** |  | [optional]
**calculate_column** | **string** |  | [optional]
**extract_column_key** | **string** |  | [optional]
**result_column_key** | **string** |  | [optional]
**table_condition** | [**\SeaTable\Client\User\ActionLookupAndCopyTableCondition**](ActionLookupAndCopyTableCondition.md) |  | [optional]
**equal_column_conditions** | [**\SeaTable\Client\User\ActionLookupAndCopyEqualColumnConditionsInner[]**](ActionLookupAndCopyEqualColumnConditionsInner.md) |  | [optional]
**fill_column_conditions** | [**\SeaTable\Client\User\ActionLookupAndCopyEqualColumnConditionsInner[]**](ActionLookupAndCopyEqualColumnConditionsInner.md) |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
