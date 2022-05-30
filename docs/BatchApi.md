# swagger_client.BatchApi

All URIs are relative to *https://api.regelleistung.net/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch**](BatchApi.md#batch) | **POST** /batch | Submit batch requests

# **batch**
> BatchResponse batch(body=body)

Submit batch requests

Batch requests take the form of a series of REST API requests. The overall result in the form of arrayed REST API responses is then returned to the client. This is useful for reducing HTTP overhead. The following conditions apply when using the batch endpoint:   * The responses to the operations are returned in the same order as requested.   * Only POST, PATCH and DELETE methods on /bids are supported.   * The number of operations per batch is limited to 100.   * Each operation is executed separately. The failure of one operation has no effect on the execution of the other operations in the batch or the processing of the overall batch. There is no transactionality across or dependency between single batch operations. E.g. one operation can fail and all following can still succeed! 

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
api_instance = swagger_client.BatchApi(swagger_client.ApiClient(configuration))
body = swagger_client.BatchRequest() # BatchRequest |  (optional)

try:
    # Submit batch requests
    api_response = api_instance.batch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchApi->batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchRequest**](BatchRequest.md)|  | [optional] 

### Return type

[**BatchResponse**](BatchResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

