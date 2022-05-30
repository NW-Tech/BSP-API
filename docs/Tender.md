# Tender

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**TenderIdentification**](TenderIdentification.md) |  | [optional] 
**product_type** | [**ProductType**](ProductType.md) |  | [optional] 
**delivery_date** | **date** | Delivery day of offered control reserve / energy. (ISO 8601 format YYYY-MM-DD). | [optional] 
**market** | [**ReserveMarket**](ReserveMarket.md) |  | [optional] 
**time_interval** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**gate_open_time** | **datetime** | Gate open time of tender. | [optional] 
**gate_closure_time** | **datetime** | Gate closure time of tender. | [optional] 
**state** | **str** | Actual state of the tender. For detailed information on the tender state model, see the [reference guide.](/docs/guide#tender-state-model) | [optional] 
**result** | **str** | Result of the tender. For detailed information on the specific tender results, see the [reference guide.](/docs/guide#tender-state-model) | [optional] 
**run_number** | **int** |  | [optional] 
**products** | [**list[ProductName]**](ProductName.md) | Available products for tender. | [optional] 
**business_rules_key** | **str** | Key to identify the current business rules for bidding. For detailed information, see the [reference guide.](/docs/guide#business-rules-key) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

