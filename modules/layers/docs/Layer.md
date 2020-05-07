# Layer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the layer | [optional] 
**path** | **str** | Location of the layer in the WMS capabilities layer tree | [optional] 
**type** | **str** | Type of published layer. Can be VECTOR, RASTER, REMOTE, WMS or GROUP. Must be consistent with resource definition. | [optional] 
**default_style** | [**StyleReference**](StyleReference.md) |  | [optional] 
**styles** | **object** | Avaialble styles for layer publication | [optional] 
**resource** | **object** | Resource supplying information for layer publication | [optional] 
**opaque** | **bool** | Controls layer transparency (whether the layer is opaque or transparent). | [optional] 
**metadata** | [**list[MetadataEntry]**](MetadataEntry.md) |  | [optional] 
**attribution** | **object** | WMS attribution information to be drawn on each map | [optional] 
**authority_ur_ls** | **list[object]** |  | [optional] 
**identifiers** | **list[object]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

