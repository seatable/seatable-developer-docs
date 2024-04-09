# # ListRowLinks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_id** | **string** | The id of the table. The id of a table is unique inside a base and is often used to identify a table. **Important: the table_id is not the table_name**. |
**link_column** | **string** | This is the key of the link column. Do not use the &#x60;link_id&#x60; of the link column here. |
**rows** | [**\SeaTable\Client\Base\ListRowLinksRowsInner[]**](ListRowLinksRowsInner.md) | the rows you want to get the links for. | [optional]

