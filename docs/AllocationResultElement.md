# AllocationResultElement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_type** | [**ProductType**](ProductType.md) |  | [optional] 
**delivery_date** | **date** | Delivery day of offered control reserve / energy. (ISO 8601 format YYYY-MM-DD). | [optional] 
**product_name** | [**ProductName**](ProductName.md) |  | [optional] 
**direction** | [**Direction**](Direction.md) |  | [optional] 
**time_interval** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**connecting_zone** | [**ConnectingZone**](ConnectingZone.md) |  | [optional] 
**market** | [**ReserveMarket**](ReserveMarket.md) |  | [optional] 
**status** | **str** |  | [optional] 
**allocation_ranking** | **int** | Specifies the allocation ranking of bids as a natural number in ascending order starting at 1. | [optional] 
**activation_ranking** | **int** | Specifies the activation ranking of accepted aFRR/mFRR bids as a natural number in ascending order starting at 1. | [optional] 
**indivisible** | **bool** |  | [optional] [default to False]
**offered_quantity** | [**Quantity**](Quantity.md) |  | [optional] 
**accepted_quantity** | [**Quantity**](Quantity.md) |  | [optional] 
**prices** | [**list[Price]**](Price.md) | Price informations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

