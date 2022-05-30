# swagger_client.HealthApi

All URIs are relative to *https://api.regelleistung.net/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_health_informations**](HealthApi.md#get_api_health_informations) | **GET** /health | API health endpoint.

# **get_api_health_informations**
> Health get_api_health_informations()

API health endpoint.

Provides information about the current availability of base functions of the IP RL platform.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HealthApi()

try:
    # API health endpoint.
    api_response = api_instance.get_api_health_informations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->get_api_health_informations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Health**](Health.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

