# BidSubmissionResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**BidIdentification**](BidIdentification.md) |  | [optional] 
**complex_bid_id** | [**BidIdentification**](BidIdentification.md) |  | [optional] 
**group_id** | [**BidIdentification**](BidIdentification.md) |  | [optional] 
**bid_type** | [**BidType**](BidType.md) |  | [optional] 
**tender** | [**TenderIdentification**](TenderIdentification.md) |  | [optional] 
**product_type** | [**ProductType**](ProductType.md) |  | [optional] 
**delivery_date** | [**DeliveryDate**](DeliveryDate.md) |  | [optional] 
**market** | [**ReserveMarket**](ReserveMarket.md) |  | [optional] 
**product_name** | [**ProductName**](ProductName.md) |  | [optional] 
**direction** | [**Direction**](Direction.md) |  | [optional] 
**time_interval** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**connecting_zone** | [**ConnectingZone**](ConnectingZone.md) |  | [optional] 
**resource_provider** | [**EIC**](EIC.md) |  | [optional] 
**status** | **str** |  | [optional] 
**receipt_timestamp** | **datetime** | Receipt time of the bid. | [optional] 
**revision_timestamp** | **datetime** | Revision timestamp of the bid. | [optional] 
**activation** | [**ActivationType**](ActivationType.md) |  | [optional] 
**min_quantity** | [**Quantity**](Quantity.md) |  | [optional] 
**offered_quantity** | [**Quantity**](Quantity.md) |  | [optional] 
**accepted_quantity** | [**Quantity**](Quantity.md) |  | [optional] 
**prices** | [**Prices**](Prices.md) |  | [optional] 
**technical_linkage** | [**TechnicalLinkage**](TechnicalLinkage.md) |  | [optional] 
**conditional_linkage** | [**ConditionalLinkage**](ConditionalLinkage.md) |  | [optional] 
**backup_for** | [**BalancingServiceProvider**](BalancingServiceProvider.md) |  | [optional] 
**tag** | [**BidTag**](BidTag.md) |  | [optional] 
**components** | [**list[Bid]**](Bid.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

