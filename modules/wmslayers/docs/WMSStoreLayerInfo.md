# WMSStoreLayerInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the layer, corresponding to the published name of the resource | [optional] 
**native_name** | **str** | Name of the layer as known on the remote WMS | [optional] 
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
**forced_remote_style** | **str** | Remote style to be used in remote GetMap request. | [optional] 
**selected_remote_formats** | **list[str]** | Additional list of image formats supported by remote WMS Server. | [optional] 
**preferred_format** | **str** | Output image format to be used in remote GetMap request | [optional] 
**selected_remote_styles** | **list[str]** | Additional list of remote styles that can be used to remote GetMap requests. | [optional] 
**all_available_remote_styles** | [**list[StyleInfo]**](StyleInfo.md) | List of complete style info objects that contain name, sld format and GetLegendRequests. | [optional] 
**min_scale** | **float** | minimum scale denominator, works like Scale denomintors in SLD. | [optional] 
**max_scale** | **float** | maximum scale denominator, works like Scale denomintors in SLD. | [optional] 
**metadata_b_box_respected** | **bool** | An optimization that skips remote GetMap requests if requested Map is outside advertised bounds. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

