# swagger_client.ResultsApi

All URIs are relative to *https://api.regelleistung.net/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_allocation_results**](ResultsApi.md#get_allocation_results) | **GET** /results | Anonymous results

# **get_allocation_results**
> list[AllocationResultElement] get_allocation_results(delivery_date=delivery_date, market=market, tender=tender, product_type=product_type, product_name=product_name, state=state, zone=zone, offset=offset, limit=limit)

Anonymous results

Returns the anonymous results of allocated tenders sorted in the following order:   * `market`,   * `productType`,   * `productName`,   * `allocationRanking`  The result list can be reduced as required by specifying combinations of different filter parameters. 

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
api_instance = swagger_client.ResultsApi(swagger_client.ApiClient(configuration))
delivery_date = '2013-10-20' # date | Only results for the specified delivery date will be listed (ISO 8601 format YYYY-MM-DD). If not specified and also no tender ID is specified, then only results for today's delivery day will be listed. (optional)
market = swagger_client.ReserveMarket() # ReserveMarket | Market filter. If not specified and also no tender ID is specified, then only bids for capacity market will be listed. (optional)
tender = swagger_client.TenderIdentification() # TenderIdentification | By specifying the tender ID, only results of this tender will be listed. (optional)
product_type = swagger_client.ProductType() # ProductType | Product type filter. If this query parameter is not set and also no tender ID is specified, results for all product types are returned. (optional)
product_name = swagger_client.ProductName() # ProductName |  (optional)
state = 'state_example' # str |  (optional)
zone = swagger_client.CountryCode() # CountryCode |  (optional)
offset = 0 # int | The number of items to skip before starting to collect the result set. (optional) (default to 0)
limit = 100 # int | The numbers of items to return (optional) (default to 100)

try:
    # Anonymous results
    api_response = api_instance.get_allocation_results(delivery_date=delivery_date, market=market, tender=tender, product_type=product_type, product_name=product_name, state=state, zone=zone, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultsApi->get_allocation_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_date** | **date**| Only results for the specified delivery date will be listed (ISO 8601 format YYYY-MM-DD). If not specified and also no tender ID is specified, then only results for today&#x27;s delivery day will be listed. | [optional] 
 **market** | [**ReserveMarket**](.md)| Market filter. If not specified and also no tender ID is specified, then only bids for capacity market will be listed. | [optional] 
 **tender** | [**TenderIdentification**](.md)| By specifying the tender ID, only results of this tender will be listed. | [optional] 
 **product_type** | [**ProductType**](.md)| Product type filter. If this query parameter is not set and also no tender ID is specified, results for all product types are returned. | [optional] 
 **product_name** | [**ProductName**](.md)|  | [optional] 
 **state** | **str**|  | [optional] 
 **zone** | [**CountryCode**](.md)|  | [optional] 
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **limit** | **int**| The numbers of items to return | [optional] [default to 100]

### Return type

[**list[AllocationResultElement]**](AllocationResultElement.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

