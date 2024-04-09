# # ArchivedRowLinks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_id** | **string** | The id of the table. The id of a table is unique inside a base and is often used to identify a table. **Important: the table_id is not the table_name**. |
**other_table_id** | **string** | The id of the table. The id of a table is unique inside a base and is often used to identify a table. **Important: the table_id is not the table_name**. |
**link_id** | **string** | Every *link column* has a &#x60;key&#x60; and &#x60;link_id&#x60; in the column object. Use [Get Metadata](/reference/get-metadata) or [Get Base Info](/reference/get-base-info) to get this &#x60;link_id&#x60;. Don&#39;t use the &#x60;key&#x60; of the link column. |
**other_rows_ids_map** | **array<string,string[]>** | Map of IDs of the target rows which you&#39;d like to link/unlink your source rows. Use a key-to-list like: &#x60;&#x60;&#x60; \&quot;other_rows_ids_map\&quot;: {   \&quot;&lt;row1 of table&gt;\&quot;: [\&quot;&lt;row1 of other_table&gt;\&quot;, \&quot;&lt;row2 of other_table&gt;\&quot;],   \&quot;&lt;row2 of table&gt;\&quot;: [\&quot;&lt;row3 of other_table&gt;\&quot;] } &#x60;&#x60;&#x60; |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
