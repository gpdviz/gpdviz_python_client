# swagger_client.StreamApi

All URIs are relative to *http://localhost:5050/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_stream**](StreamApi.md#delete_stream) | **DELETE** /ss/{sysid}/{strid} | Delete a data stream
[**get_stream**](StreamApi.md#get_stream) | **GET** /ss/{sysid}/{strid} | Get a data stream
[**register_stream**](StreamApi.md#register_stream) | **POST** /ss/{sysid} | Add a data stream


# **delete_stream**
> SensorSystem delete_stream(sysid, strid)

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
    api_response = api_instance.delete_stream(sysid, strid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->delete_stream: %s\n" % e)
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

# **get_stream**
> DataStream get_stream(sysid, strid)

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
    api_response = api_instance.get_stream(sysid, strid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->get_stream: %s\n" % e)
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

# **register_stream**
> SensorSystem register_stream(sysid, body)

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
    api_response = api_instance.register_stream(sysid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->register_stream: %s\n" % e)
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

