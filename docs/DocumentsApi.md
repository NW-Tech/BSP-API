# swagger_client.DocumentsApi

All URIs are relative to *https://api.regelleistung.net/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_document**](DocumentsApi.md#get_document) | **GET** /documents/{id} | Returns a document by its id.
[**get_document_content**](DocumentsApi.md#get_document_content) | **GET** /documents/{id}/content | Returns the content of requested document as \&quot;file download\&quot;
[**get_documents**](DocumentsApi.md#get_documents) | **GET** /documents | Result documents

# **get_document**
> ResultDocument get_document(id)

Returns a document by its id.

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
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
id = swagger_client.ResourceIdentification() # ResourceIdentification | Document identification

try:
    # Returns a document by its id.
    api_response = api_instance.get_document(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ResourceIdentification**](.md)| Document identification | 

### Return type

[**ResultDocument**](ResultDocument.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_content**
> str get_document_content(id)

Returns the content of requested document as \"file download\"

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
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
id = swagger_client.ResourceIdentification() # ResourceIdentification | Document identification

try:
    # Returns the content of requested document as \"file download\"
    api_response = api_instance.get_document_content(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_document_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ResourceIdentification**](.md)| Document identification | 

### Return type

**str**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents**
> list[ResultDocument] get_documents(delivery_date=delivery_date, tender=tender, market=market, product_type=product_type, tag=tag, offset=offset, limit=limit)

Result documents

File archive interface of final result documents.

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
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
delivery_date = '2013-10-20' # date | Only documents for the specified delivery date are listed (ISO 8601 format YYYY-MM-DD). If not specified and also no tender ID is specified, then only documents for today's delivery day will be listed. (optional)
tender = swagger_client.TenderIdentification() # TenderIdentification | Tender Id filter. (optional)
market = swagger_client.ReserveMarket() # ReserveMarket | If not specified and also no tender ID is specified, documents for all markets are returned. (optional)
product_type = swagger_client.ProductType() # ProductType | Product type filter. If this query parameter is not set and also no tender ID is specified, documents for all product types are returned. (optional)
tag = 'tag_example' # str | Tag filter. If this query parameter is not set, values for all tags are returned. (optional)
offset = 0 # int | The number of items to skip before starting to collect the result set. (optional) (default to 0)
limit = 100 # int | The numbers of items to return (optional) (default to 100)

try:
    # Result documents
    api_response = api_instance.get_documents(delivery_date=delivery_date, tender=tender, market=market, product_type=product_type, tag=tag, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_date** | **date**| Only documents for the specified delivery date are listed (ISO 8601 format YYYY-MM-DD). If not specified and also no tender ID is specified, then only documents for today&#x27;s delivery day will be listed. | [optional] 
 **tender** | [**TenderIdentification**](.md)| Tender Id filter. | [optional] 
 **market** | [**ReserveMarket**](.md)| If not specified and also no tender ID is specified, documents for all markets are returned. | [optional] 
 **product_type** | [**ProductType**](.md)| Product type filter. If this query parameter is not set and also no tender ID is specified, documents for all product types are returned. | [optional] 
 **tag** | **str**| Tag filter. If this query parameter is not set, values for all tags are returned. | [optional] 
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **limit** | **int**| The numbers of items to return | [optional] [default to 100]

### Return type

[**list[ResultDocument]**](ResultDocument.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

