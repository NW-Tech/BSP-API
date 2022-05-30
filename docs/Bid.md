# Bid

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**BidIdentification**](BidIdentification.md) |  | 
**complex_bid_id** | [**BidIdentification**](BidIdentification.md) |  | [optional] 
**group_id** | [**BidIdentification**](BidIdentification.md) |  | [optional] 
**bid_type** | [**BidType**](BidType.md) |  | 
**tender** | [**TenderIdentification**](TenderIdentification.md) |  | 
**product_type** | [**ProductType**](ProductType.md) |  | 
**delivery_date** | [**DeliveryDate**](DeliveryDate.md) |  | 
**market** | [**ReserveMarket**](ReserveMarket.md) |  | 
**product_name** | [**ProductName**](ProductName.md) |  | 
**direction** | [**Direction**](Direction.md) |  | 
**time_interval** | [**TimeInterval**](TimeInterval.md) |  | 
**connecting_zone** | [**ConnectingZone**](ConnectingZone.md) |  | 
**resource_provider** | [**EIC**](EIC.md) |  | 
**status** | **str** |  | 
**receipt_timestamp** | **datetime** | Receipt time of the bid. | 
**revision_timestamp** | **datetime** | Revision timestamp of the bid. | 
**activation** | [**ActivationType**](ActivationType.md) |  | [optional] 
**min_quantity** | [**Quantity**](Quantity.md) |  | [optional] 
**offered_quantity** | [**Quantity**](Quantity.md) |  | 
**accepted_quantity** | [**Quantity**](Quantity.md) |  | [optional] 
**prices** | [**Prices**](Prices.md) |  | 
**technical_linkage** | [**TechnicalLinkage**](TechnicalLinkage.md) |  | [optional] 
**conditional_linkage** | [**ConditionalLinkage**](ConditionalLinkage.md) |  | [optional] 
**backup_for** | [**BalancingServiceProvider**](BalancingServiceProvider.md) |  | [optional] 
**tag** | [**BidTag**](BidTag.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

