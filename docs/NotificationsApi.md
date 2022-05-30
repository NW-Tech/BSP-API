# swagger_client.NotificationsApi

All URIs are relative to *https://api.regelleistung.net/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_notifications**](NotificationsApi.md#get_notifications) | **GET** /notifications | Notifications

# **get_notifications**
> list[Notification] get_notifications(product_type=product_type, after=after, limit=limit)

Notifications

Returns new notifications about the tendering process since the given datetime parameter. The result list is ordered by publishing time descending.

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
api_instance = swagger_client.NotificationsApi(swagger_client.ApiClient(configuration))
product_type = 'product_type_example' # str | Product type filter for notifications. If not specified, then notifications for all product types are returned. (optional)
after = '2013-10-20T19:20:30+01:00' # datetime | Oldest publishing time of notfications to be returned. If not specified, then only notifications within the last 24 hours are returned. (optional)
limit = 100 # int | The numbers of items to return (optional) (default to 100)

try:
    # Notifications
    api_response = api_instance.get_notifications(product_type=product_type, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_type** | **str**| Product type filter for notifications. If not specified, then notifications for all product types are returned. | [optional] 
 **after** | **datetime**| Oldest publishing time of notfications to be returned. If not specified, then only notifications within the last 24 hours are returned. | [optional] 
 **limit** | **int**| The numbers of items to return | [optional] [default to 100]

### Return type

[**list[Notification]**](Notification.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

