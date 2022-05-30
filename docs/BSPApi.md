# swagger_client.BSPApi

All URIs are relative to *https://api.regelleistung.net/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_backup_contracts**](BSPApi.md#get_backup_contracts) | **GET** /backup-contracts | Returns current backup contracts
[**get_framework_contracts**](BSPApi.md#get_framework_contracts) | **GET** /framework-agreements | Current framework agreements
[**get_pre_qualified_capacities**](BSPApi.md#get_pre_qualified_capacities) | **GET** /pre-qualified-capacities/{deliveryDate} | Prequalified capacities.

# **get_backup_contracts**
> list[BackupContract] get_backup_contracts(valid_date=valid_date, product_type=product_type)

Returns current backup contracts

Returns valid backup contracts.

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
api_instance = swagger_client.BSPApi(swagger_client.ApiClient(configuration))
valid_date = '2013-10-20' # date | Contracts for a specified day can be queried. If not specified, contracts for today will be listed. (optional)
product_type = 'product_type_example' # str | Product type filter for contracts. If not specified, then contracts for all product types are returned. (optional)

try:
    # Returns current backup contracts
    api_response = api_instance.get_backup_contracts(valid_date=valid_date, product_type=product_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BSPApi->get_backup_contracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **valid_date** | **date**| Contracts for a specified day can be queried. If not specified, contracts for today will be listed. | [optional] 
 **product_type** | **str**| Product type filter for contracts. If not specified, then contracts for all product types are returned. | [optional] 

### Return type

[**list[BackupContract]**](BackupContract.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_framework_contracts**
> list[FrameworkAgreement] get_framework_contracts(product_type=product_type)

Current framework agreements

Returns current framework agreements.

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
api_instance = swagger_client.BSPApi(swagger_client.ApiClient(configuration))
product_type = 'product_type_example' # str | Product type filter for framework agreements. If this query parameter is not set, contracts for all product types are returned. (optional)

try:
    # Current framework agreements
    api_response = api_instance.get_framework_contracts(product_type=product_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BSPApi->get_framework_contracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_type** | **str**| Product type filter for framework agreements. If this query parameter is not set, contracts for all product types are returned. | [optional] 

### Return type

[**list[FrameworkAgreement]**](FrameworkAgreement.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pre_qualified_capacities**
> list[PrequalifiedCapacity] get_pre_qualified_capacities(delivery_date, product_type=product_type)

Prequalified capacities.

Returns my pre-qualified capacities in each control area (sum of PTU capacities) valid on specific delivery date.

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
api_instance = swagger_client.BSPApi(swagger_client.ApiClient(configuration))
delivery_date = '2013-10-20' # date | Defines the delivery date for which the pre-qualified capacities are to be returned.
product_type = 'product_type_example' # str | Product type filter for contracts. If not specified, then contracts for all product types are returned. (optional)

try:
    # Prequalified capacities.
    api_response = api_instance.get_pre_qualified_capacities(delivery_date, product_type=product_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BSPApi->get_pre_qualified_capacities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_date** | **date**| Defines the delivery date for which the pre-qualified capacities are to be returned. | 
 **product_type** | **str**| Product type filter for contracts. If not specified, then contracts for all product types are returned. | [optional] 

### Return type

[**list[PrequalifiedCapacity]**](PrequalifiedCapacity.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

