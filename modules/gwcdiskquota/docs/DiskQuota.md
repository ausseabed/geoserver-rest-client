# DiskQuota

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Determines if Disk Quota is to be used. | [optional] 
**disk_block_size** | **float** | The number of bytes allocated to Disk Quota. | [optional] 
**cache_clean_up_frequency** | **float** | GeoWebCache will not truncate the cache as soon as the disk quota is exceeded. Instead, it polls the store at given intervals, with this time interval set. | [optional] 
**cache_clean_up_units** | **str** | The time unit used to describe the number in cacheCleanUpFrequency. | [optional] 
**max_concurrent_clean_ups** | **float** | The amount of threads to use when processing the disk quota. | [optional] 
**global_expiration_policy_name** | **str** | When a disk quota is reached, further tiles will be saved at the expense of other tiles which will be truncated. The Least Frequently Used (LFU) policy will analyze the disk quota page store and delete the pages of tiles that have been accessed the least often. The Least Recently Used (LRU) policy will analyze the diskquota page store and delete the tiles that haven’t been accessed in the longest amount of time. | [optional] 
**global_quota** | **object** | When the global quota is exceeded, first any explicitly configured quota is enforced, and then the global quota is enforced acting upon all the remaining layers until the global quota is reached back. | [optional] 
**layer_quota** | **object** | When a layer&#x27;s disk quota is reached, further tiles will be saved at the expense of other tiles which will be truncated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

