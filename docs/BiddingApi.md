# swagger_client.BiddingApi

All URIs are relative to *https://api.regelleistung.net/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_bid**](BiddingApi.md#delete_bid) | **DELETE** /bids/{id} | Deletes a simple, complex bid or a bid component
[**get_bid**](BiddingApi.md#get_bid) | **GET** /bids/{id} | Get a simple, complex bid or a complex bid component
[**get_bids**](BiddingApi.md#get_bids) | **GET** /bids | List submitted bids (optionally capacity or energy market)
[**submit_bid**](BiddingApi.md#submit_bid) | **POST** /bids | Submit a simple, complex bid or a complex bid component
[**update_bid**](BiddingApi.md#update_bid) | **PATCH** /bids/{id} | Updates a simple, complex bid or a bid component

# **delete_bid**
> delete_bid(id)

Deletes a simple, complex bid or a bid component

This operation can be used to delete   * a specific simple bid (with the unique ID of the bid),   * a single component of a complex bid (with the unique ID of the bid component) or   * the entire complex bid with all its components (with the group ID of the complex bid). 

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
api_instance = swagger_client.BiddingApi(swagger_client.ApiClient(configuration))
id = swagger_client.BidIdentification() # BidIdentification | Bid identification

try:
    # Deletes a simple, complex bid or a bid component
    api_instance.delete_bid(id)
except ApiException as e:
    print("Exception when calling BiddingApi->delete_bid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**BidIdentification**](.md)| Bid identification | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bid**
> Bid get_bid(id)

Get a simple, complex bid or a complex bid component

Returns the single bid with requested ID

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
api_instance = swagger_client.BiddingApi(swagger_client.ApiClient(configuration))
id = swagger_client.BidIdentification() # BidIdentification | Unique bid identification or group bid id of complex bid

try:
    # Get a simple, complex bid or a complex bid component
    api_response = api_instance.get_bid(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiddingApi->get_bid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**BidIdentification**](.md)| Unique bid identification or group bid id of complex bid | 

### Return type

[**Bid**](Bid.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bids**
> list[Bid] get_bids(delivery_date=delivery_date, market=market, tender=tender, product_type=product_type, product_name=product_name, state=state, zone=zone, _from=_from, to=to, type=type, cid=cid, gid=gid, link=link, linked_to=linked_to, tag=tag, backups_only=backups_only, backup_for=backup_for, offset=offset, limit=limit)

List submitted bids (optionally capacity or energy market)

Returns the list of all submitted capacity/energy bids and complex bid components sorted in the following order:   * `productType`,   * `productName`,   * `state`,   * `revisionTimestamp`,   * `id`.  The result list can be reduced as required by specifying combinations of different filter parameters. 

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
api_instance = swagger_client.BiddingApi(swagger_client.ApiClient(configuration))
delivery_date = '2013-10-20' # date | Only bids for the specified delivery date will be listed (ISO 8601 format YYYY-MM-DD). If not specified and also no tender ID is specified, then only bids for today's delivery day will be listed. (optional)
market = swagger_client.ReserveMarket() # ReserveMarket | Market filter. If not specified and also no tender ID is specified, then only bids for capacity market will be listed. (optional)
tender = swagger_client.TenderIdentification() # TenderIdentification | By specifying the tender ID, only bids of this tender will be listed. For details on the tender id format, see the [reference guide.](/docs/guide#tender-id) (optional)
product_type = swagger_client.ProductType() # ProductType | Product type filter. If this query parameter is not set and also no tender ID is specified, bids for all product types are returned. (optional)
product_name = swagger_client.ProductName() # ProductName | Product name filter. If this query parameter is not set, bids for all product names are returned. (optional)
state = 'state_example' # str |  (optional)
zone = swagger_client.EIC() # EIC |  (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
type = swagger_client.BidType() # BidType | By specifying the type, only bids of this type will be listed. (optional)
cid = swagger_client.BidIdentification() # BidIdentification | Filters bids that have the given complex bid ID. (optional)
gid = swagger_client.BidIdentification() # BidIdentification | Filters bids that have the given bid group ID. (optional)
link = swagger_client.TechnicalLinkIdentification() # TechnicalLinkIdentification | Filters bids that have the given technical link ID. (optional)
linked_to = swagger_client.BidIdentification() # BidIdentification | Filters bids that have a conditional link to the given bid ID. (optional)
tag = swagger_client.BidTag() # BidTag | Filters bids that have the given tag. (optional)
backups_only = false # bool |  (optional) (default to false)
backup_for = swagger_client.EIC() # EIC | Filters bids which are a backup for the provider with the given EIC (optional)
offset = 0 # int | The number of items to skip before starting to collect the result set. (optional) (default to 0)
limit = 100 # int | The numbers of items to return (optional) (default to 100)

try:
    # List submitted bids (optionally capacity or energy market)
    api_response = api_instance.get_bids(delivery_date=delivery_date, market=market, tender=tender, product_type=product_type, product_name=product_name, state=state, zone=zone, _from=_from, to=to, type=type, cid=cid, gid=gid, link=link, linked_to=linked_to, tag=tag, backups_only=backups_only, backup_for=backup_for, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiddingApi->get_bids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_date** | **date**| Only bids for the specified delivery date will be listed (ISO 8601 format YYYY-MM-DD). If not specified and also no tender ID is specified, then only bids for today&#x27;s delivery day will be listed. | [optional] 
 **market** | [**ReserveMarket**](.md)| Market filter. If not specified and also no tender ID is specified, then only bids for capacity market will be listed. | [optional] 
 **tender** | [**TenderIdentification**](.md)| By specifying the tender ID, only bids of this tender will be listed. For details on the tender id format, see the [reference guide.](/docs/guide#tender-id) | [optional] 
 **product_type** | [**ProductType**](.md)| Product type filter. If this query parameter is not set and also no tender ID is specified, bids for all product types are returned. | [optional] 
 **product_name** | [**ProductName**](.md)| Product name filter. If this query parameter is not set, bids for all product names are returned. | [optional] 
 **state** | **str**|  | [optional] 
 **zone** | [**EIC**](.md)|  | [optional] 
 **_from** | **datetime**|  | [optional] 
 **to** | **datetime**|  | [optional] 
 **type** | [**BidType**](.md)| By specifying the type, only bids of this type will be listed. | [optional] 
 **cid** | [**BidIdentification**](.md)| Filters bids that have the given complex bid ID. | [optional] 
 **gid** | [**BidIdentification**](.md)| Filters bids that have the given bid group ID. | [optional] 
 **link** | [**TechnicalLinkIdentification**](.md)| Filters bids that have the given technical link ID. | [optional] 
 **linked_to** | [**BidIdentification**](.md)| Filters bids that have a conditional link to the given bid ID. | [optional] 
 **tag** | [**BidTag**](.md)| Filters bids that have the given tag. | [optional] 
 **backups_only** | **bool**|  | [optional] [default to false]
 **backup_for** | [**EIC**](.md)| Filters bids which are a backup for the provider with the given EIC | [optional] 
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **limit** | **int**| The numbers of items to return | [optional] [default to 100]

### Return type

[**list[Bid]**](Bid.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_bid**
> BidSubmissionResponse submit_bid(body=body)

Submit a simple, complex bid or a complex bid component

Submission of a simple or complex bid for a open capacity/energy market tender. By specifying the product, delivery date and market, the bid is automatically assigned to the corresponding open tender. The gate closure time of the tender is relevant for the submission.

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
api_instance = swagger_client.BiddingApi(swagger_client.ApiClient(configuration))
body = swagger_client.BidSubmission() # BidSubmission |  (optional)

try:
    # Submit a simple, complex bid or a complex bid component
    api_response = api_instance.submit_bid(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiddingApi->submit_bid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BidSubmission**](BidSubmission.md)|  | [optional] 

### Return type

[**BidSubmissionResponse**](BidSubmissionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bid**
> Bid update_bid(id, body=body)

Updates a simple, complex bid or a bid component

Connecting zone, volumes and prices can be changed (only applies to simple bids and individual components of a complex bid). Furthermore, linkages can be defined. The validation rules apply as for bid submission. It is possible to only include necessary information (change) in the request body, thus omitting bid attributes which are not to be changed.

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
api_instance = swagger_client.BiddingApi(swagger_client.ApiClient(configuration))
id = swagger_client.BidIdentification() # BidIdentification | Bid identification
body = swagger_client.BidModification() # BidModification |  (optional)

try:
    # Updates a simple, complex bid or a bid component
    api_response = api_instance.update_bid(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiddingApi->update_bid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**BidIdentification**](.md)| Bid identification | 
 **body** | [**BidModification**](BidModification.md)|  | [optional] 

### Return type

[**Bid**](Bid.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

