# # ActionRecordsMeetSpecificConditionsAfterModificationInner

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
**row** | [**\SeaTable\Client\User\ActionAddRecordToOtherTableRow**](ActionAddRecordToOtherTableRow.md) |  | [optional]
**is_locked** | **string** |  | [optional]
**updates** | **array<string,string>** | Is an object including the column key and desired content of each field that you would like to modify. | [optional]
**link_id** | **string** |  | [optional]
**linked_table_id** | **string** |  | [optional]
**match_conditions** | [**\SeaTable\Client\User\ActionLinkRecordMatchConditionsInner[]**](ActionLinkRecordMatchConditionsInner.md) |  | [optional]
**dst_table_id** | **string** |  | [optional]
**script_name** | **string** |  | [optional]
**workspace_id** | **int** |  | [optional]
**owner** | **string** |  | [optional]
**org_id** | **int** |  | [optional]
**repo_id** | **string** |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
