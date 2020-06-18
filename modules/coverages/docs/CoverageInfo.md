# CoverageInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the resource. This name corresponds to the \&quot;published\&quot; name of the resource. | [optional] 
**native_name** | **str** | The native name of the resource. This name corresponds to the physical resource that feature type is derived from -- a shapefile name, a database table, etc... | [optional] 
**native_format** | **str** | The native format of the resource (e.g. GEOTIFF) | [optional] 
**namespace** | **object** | The namespace uri of the resource. Example would be an application schema namespace uri. | [optional] 
**title** | **str** | The title of the resource. This is usually something that is meant to be displayed in a user interface. | [optional] 
**abstract** | **str** | A description of the resource. This is usually something that is meant to be displayed in a user interface. | [optional] 
**default_interpolation_method** | **str** | Default resampling (interpolation) method that will be used for this coverage. | [optional] 
**keywords** | **object** | A collection of keywords associated with the resource. | [optional] 
**supported_formats** | **object** | A collection of supported formats associated with the resource. | [optional] 
**metadata_links** | **object** | Wraps a collection of metadata links for the resource. | [optional] 
**data_links** | **object** | Wraps a collection of data links for the resource. | [optional] 
**native_crs** | **str** | The native coordinate reference system object of the resource. | [optional] 
**srs** | **str** | Returns the identifier of coordinate reference system of the resource. | [optional] 
**native_bounding_box** | **object** | Returns the bounds of the resource in its declared CRS. | [optional] 
**lat_lon_bounding_box** | **object** | The bounds of the resource in lat / lon. This value represents a \&quot;fixed value\&quot; and is not calulated on the underlying dataset. | [optional] 
**metadata** | [**list[MetadataEntry]**](MetadataEntry.md) | A list of key/value metadata pairs. | [optional] 
**store** | **object** | The store the resource is a part of. | [optional] 
**cql_filter** | **str** | The ECQL string used as default feature type filter | [optional] 
**max_features** | **int** | A cap on the number of features that a query against this type can return. | [optional] 
**num_decimals** | **float** | The number of decimal places to use when encoding floating point numbers from data of this feature type. | [optional] 
**request_srs** | **object** | The srs&#x27;s that the WFS service will advertise in the capabilities document for this feature type (overriding the global WFS settings). | [optional] 
**response_srs** | **object** | The srs&#x27;s that the WFS service will advertise in the capabilities document for this feature type (overriding the global WFS settings). | [optional] 
**overriding_service_srs** | **bool** | True if this feature type info is overriding the WFS global SRS list | [optional] 
**skip_number_matched** | **bool** | True if this feature type info is overriding the counting of numberMatched. | [optional] 
**circular_arc_present** | **bool** |  | [optional] 
**linearization_tolerance** | **float** | Tolerance used to linearize this feature type, as an absolute value expressed in the geometries own CRS | [optional] 
**attributes** | **object** | Wrapper for the derived set of attributes for the feature type. | [optional] 
**dimensions** | **object** | raster dimensions | [optional] 
**grid** | **object** | contains information about how to translate from the raster plan to a coordinate reference system | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

