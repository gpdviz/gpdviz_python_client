# swagger_client.StreamApi

All URIs are relative to *http://tsauv.shore.mbari.org/gpdviz/api/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_str**](StreamApi.md#add_str) | **POST** /ss/{sysid} | Add a data stream
[**delete_str**](StreamApi.md#delete_str) | **DELETE** /ss/{sysid}/{strid} | Delete a data stream
[**get_str**](StreamApi.md#get_str) | **GET** /ss/{sysid}/{strid} | Get a data stream


# **add_str**
> SensorSystem add_str(sysid, body)

Add a data stream



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamApi()
sysid = 'sysid_example' # str | sensor system id
body = swagger_client.StreamRegister() # StreamRegister | stream definition

try: 
    # Add a data stream
    api_response = api_instance.add_str(sysid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->add_str: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sysid** | **str**| sensor system id | 
 **body** | [**StreamRegister**](StreamRegister.md)| stream definition | 

### Return type

[**SensorSystem**](SensorSystem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_str**
> SensorSystem delete_str(sysid, strid)

Delete a data stream



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamApi()
sysid = 'sysid_example' # str | sensor system id
strid = 'strid_example' # str | data stream id

try: 
    # Delete a data stream
    api_response = api_instance.delete_str(sysid, strid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->delete_str: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sysid** | **str**| sensor system id | 
 **strid** | **str**| data stream id | 

### Return type

[**SensorSystem**](SensorSystem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_str**
> DataStream get_str(sysid, strid)

Get a data stream



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StreamApi()
sysid = 'sysid_example' # str | sensor system id
strid = 'strid_example' # str | data stream id

try: 
    # Get a data stream
    api_response = api_instance.get_str(sysid, strid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->get_str: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sysid** | **str**| sensor system id | 
 **strid** | **str**| data stream id | 

### Return type

[**DataStream**](DataStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
