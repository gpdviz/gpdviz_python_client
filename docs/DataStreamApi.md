# swagger_client.DataStreamApi

All URIs are relative to *http://localhost:5050/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_stream**](DataStreamApi.md#delete_stream) | **DELETE** /ss/{sysid}/{strid} | Delete a data stream
[**get_stream**](DataStreamApi.md#get_stream) | **GET** /ss/{sysid}/{strid} | Get a data stream
[**register_stream**](DataStreamApi.md#register_stream) | **POST** /ss/{sysid} | Add a data stream


# **delete_stream**
> DataStreamSummary delete_stream(sysid, strid)

Delete a data stream



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStreamApi()
sysid = 'sysid_example' # str | sensor system id
strid = 'strid_example' # str | data stream id

try: 
    # Delete a data stream
    api_response = api_instance.delete_stream(sysid, strid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStreamApi->delete_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sysid** | **str**| sensor system id | 
 **strid** | **str**| data stream id | 

### Return type

[**DataStreamSummary**](DataStreamSummary.md)

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
api_instance = swagger_client.DataStreamApi()
sysid = 'sysid_example' # str | sensor system id
strid = 'strid_example' # str | data stream id

try: 
    # Get a data stream
    api_response = api_instance.get_stream(sysid, strid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStreamApi->get_stream: %s\n" % e)
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
> DataStreamSummary register_stream(sysid, body)

Add a data stream



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStreamApi()
sysid = 'sysid_example' # str | sensor system id
body = swagger_client.DataStreamAdd() # DataStreamAdd | stream definition

try: 
    # Add a data stream
    api_response = api_instance.register_stream(sysid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStreamApi->register_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sysid** | **str**| sensor system id | 
 **body** | [**DataStreamAdd**](DataStreamAdd.md)| stream definition | 

### Return type

[**DataStreamSummary**](DataStreamSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

