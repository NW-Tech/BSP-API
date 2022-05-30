# swagger_client.TendersApi

All URIs are relative to *https://api.regelleistung.net/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tender**](TendersApi.md#get_tender) | **GET** /tenders/{id} | Get tender
[**get_tender_demand**](TendersApi.md#get_tender_demand) | **GET** /tenders/{id}/demands | Demand of tender
[**get_tender_list**](TendersApi.md#get_tender_list) | **GET** /tenders | List tenders (optionally capacity/energy market)

# **get_tender**
> Tender get_tender(id)

Get tender

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TendersApi(swagger_client.ApiClient(configuration))
id = swagger_client.TenderIdentification() # TenderIdentification | Identificiation of requested tender. (For details on the new tender id format, see the [reference guide.](/docs/guide#tender-id))

try:
    # Get tender
    api_response = api_instance.get_tender(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TendersApi->get_tender: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TenderIdentification**](.md)| Identificiation of requested tender. (For details on the new tender id format, see the [reference guide.](/docs/guide#tender-id)) | 

### Return type

[**Tender**](Tender.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tender_demand**
> list[Demand] get_tender_demand(id)

Demand of tender

Returns the specific demand of the tender.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TendersApi(swagger_client.ApiClient(configuration))
id = swagger_client.TenderIdentification() # TenderIdentification | Identificiation of requested tender. (For details on the new tender id format, see the [reference guide.](/docs/guide#tender-id))

try:
    # Demand of tender
    api_response = api_instance.get_tender_demand(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TendersApi->get_tender_demand: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TenderIdentification**](.md)| Identificiation of requested tender. (For details on the new tender id format, see the [reference guide.](/docs/guide#tender-id)) | 

### Return type

[**list[Demand]**](Demand.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tender_list**
> list[Tender] get_tender_list(delivery_date=delivery_date, market=market, product_type=product_type)

List tenders (optionally capacity/energy market)

Returns the list of capacity/energy market tenders sorted in the following order:   * `gateClosureTime`,   * `productType`.  The result list can be reduced as required by specifying combinations of different filter parameters. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TendersApi(swagger_client.ApiClient(configuration))
delivery_date = '2013-10-20' # date | Only tenders for the specified delivery date are listed (ISO 8601 format YYYY-MM-DD). If not specified, then only tenders for today and tomorrow are listed. (optional)
market = swagger_client.ReserveMarket() # ReserveMarket | If not specified, then only tenders for capacity market will be listed. (optional)
product_type = swagger_client.ProductType() # ProductType | Product type filter. If this query parameter is not set, tenders for all product types are returned. (optional)

try:
    # List tenders (optionally capacity/energy market)
    api_response = api_instance.get_tender_list(delivery_date=delivery_date, market=market, product_type=product_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TendersApi->get_tender_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_date** | **date**| Only tenders for the specified delivery date are listed (ISO 8601 format YYYY-MM-DD). If not specified, then only tenders for today and tomorrow are listed. | [optional] 
 **market** | [**ReserveMarket**](.md)| If not specified, then only tenders for capacity market will be listed. | [optional] 
 **product_type** | [**ProductType**](.md)| Product type filter. If this query parameter is not set, tenders for all product types are returned. | [optional] 

### Return type

[**list[Tender]**](Tender.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

