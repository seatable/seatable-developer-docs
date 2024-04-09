# # UpdateTeamUserRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_staff** | **bool** | &#x60;true&#x60; or &#x60;false&#x60; if the user will be an (system) admin. &#x60;false&#x60; by default. | [optional] [default to false]
**is_admin** | **bool** | &#x60;true&#x60; or &#x60;false&#x60; if the user will be an (team) admin. &#x60;false&#x60; by default. | [optional] [default to false]
**is_active** | **bool** | &#x60;true&#x60; or &#x60;false&#x60; if the user could log in. &#x60;true&#x60; by default. | [optional] [default to true]
**role** | **string** | Update their role. For details about roles, refer to [SeaTable Roles and Permissions](https://manual.seatable.io/config/enterprise/roles_permissions/). | [optional]
**name** | **string** | Full name of the user. | [optional]
**login_id** | **string** | Optional login ID. Valid only if the system configuration allows login ID. | [optional]
**contact_email** | **string** | The contact email address of the user. | [optional]
**id_in_org** | **string** | The team ID of the user, could be a student&#39;s ID or employee ID. String. | [optional]
**unit** | **string** | Business unit. Only valid if the system configuration allows the feature. | [optional]
**password** | **string** | Login password of the user. | [optional]
**institution** | **string** | Institution. Only valid if the system configuration allows the feature. | [optional]
**row_limit** | **int** | User&#39;s total row limit in number. For example 10000. | [optional]
**quota_total** | **string** | Update their total quota in MB. | [optional]
**asset_quota_mb** | **string** | The asset quota in MB. | [optional]

