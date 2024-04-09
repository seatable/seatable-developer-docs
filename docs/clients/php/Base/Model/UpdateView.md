# # UpdateView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **string** | The new name of the view, if you want to give the view a new name. | [optional]
**is_locked** | **bool** |  | [optional]
**filters** | [**\SeaTable\Client\Base\UpdateViewFiltersInner[]**](UpdateViewFiltersInner.md) | filter of your view | [optional]
**filter_conjunction** | [**\SeaTable\Client\Base\FilterConjunction**](FilterConjunction.md) |  | [optional]
**sorts** | [**\SeaTable\Client\Base\SortsInner[]**](SortsInner.md) | sorting of your view | [optional]
**groupbys** | [**\SeaTable\Client\Base\SortsInner[]**](SortsInner.md) | grouping of your view | [optional]
**hidden_columns** | **string[]** | IDs of the rows that should be hidden | [optional]

