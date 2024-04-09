# # ListRowLinksRowsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_id** | **string** | The id of the row. The id of a row is unique inside a base and is often used to identify one specific row. | [optional]
**offset** | **int** | offset is the beginning number of your query. If your record is linked to multiple records, use e.g. 0 to start quering from the 1st element or e.g. 5 to start querying from the 6th element, etc. Attention: The returned list of linked rows is not ordered by its original order on the web interface, but rather by created time (ctime). | [optional]
**limit** | **int** | limit lets you to set a limit to the number of records returned. Use e.g. 10 to return no more than 10 records. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
