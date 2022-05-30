# Price

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Specify the amount. | 
**measure_unit** | **str** | The unit of measurement underlying the price (MW per unit (code MAW), MWh per unit (code MWH)) is used to differentiate between capacity fees (EUR/MW) and energy prices (EUR/MWh). The units of measurement are in accordance with UN/ECE Recommendation 20. | 
**resolution** | **str** | Capacity price resolution in ISO 8601 format. This field is read-only for control purposes. It is determined automatically depending on the modalities applicable to the tender. | [optional] 
**currency** | **str** | The currency in which the monetary amount is expressed. The maximum length of this information is 3 alphanumeric characters respecting the standard ISO 4217. | [optional] [default to 'EUR']
**payment_direction** | **str** | The direction of payment for activated control power relates to the energy price only (measureUnit &#x3D; MWH). | [optional] [default to 'GRID_TO_PROVIDER']
**type** | **str** | Type of price. When bidding, the type must have the value &#x60;OFFER&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

