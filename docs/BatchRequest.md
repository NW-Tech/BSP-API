# BatchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ops** | [**list[BatchOperation]**](BatchOperation.md) | List of operations to be processed. | 
**parallel** | **bool** | If true, then the operations can be executed in arbitrary order and in parallel. If false, then serial execution in request order will be enforced. This property has no impact on the results order in the batch response object. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

