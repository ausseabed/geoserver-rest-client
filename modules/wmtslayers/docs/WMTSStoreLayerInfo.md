# WMTSStoreLayerInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the layer, corresponding to the published name of the resource | [optional] 
**native_name** | **str** | Name of the layer as known on the remote WMTS | [optional] 
**namespace** | **object** | Namespace of the layer | [optional] 
**title** | **str** | Title of the layer | [optional] 
**abstract** | **str** | Description of the layer | [optional] 
**description** | **str** | Same as abstract | [optional] 
**keywords** | **list[object]** | Collection of keywords associated with the layer | [optional] 
**metadatalinks** | **object** | Wraps a collection of metadata links | [optional] 
**data_links** | **object** | Wraps a collection of data links | [optional] 
**native_crs** | **str** | Native coordinate reference system object in WKT | [optional] 
**srs** | **str** | Identifier of coordinate reference system | [optional] 
**native_bounding_box** | **object** | Bounds of the layer in its declared CRS. | [optional] 
**lat_lon_bounding_box** | **object** | Bounds of the layer in latitude / longitude. This value represents a \&quot;fixed value\&quot; and is not calculated. | [optional] 
**projection_policy** | **str** | How to handle the coordinate reference system (native versus declared) | [optional] 
**enabled** | **bool** | Whether the layer is enabled | [optional] 
**metadata** | [**list[MetadataEntry]**](MetadataEntry.md) | A list of key/value metadata pairs. | [optional] 
**store** | **object** | Store conaining the resource | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

