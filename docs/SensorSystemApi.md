# swagger_client.SensorSystemApi

All URIs are relative to *http://localhost:5050/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system**](SensorSystemApi.md#delete_system) | **DELETE** /ss/{sysid} | Unregister a sensor system
[**get_system**](SensorSystemApi.md#get_system) | **GET** /ss/{sysid} | Get a sensor system
[**list_systems**](SensorSystemApi.md#list_systems) | **GET** /ss | List all registered sensor systems
[**register_stream**](SensorSystemApi.md#register_stream) | **POST** /ss/{sysid} | Add a data stream
[**register_system**](SensorSystemApi.md#register_system) | **POST** /ss | Register sensor system
[**update_system**](SensorSystemApi.md#update_system) | **PUT** /ss/{sysid} | Update a sensor system


# **delete_system**
> SensorSystemSummary delete_system(sysid)

Unregister a sensor system



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SensorSystemApi()
sysid = 'sysid_example' # str | sensor system id

try: 
    # Unregister a sensor system
    api_response = api_instance.delete_system(sysid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorSystemApi->delete_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sysid** | **str**| sensor system id | 

### Return type

[**SensorSystemSummary**](SensorSystemSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system**
> SensorSystem get_system(sysid)

Get a sensor system



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SensorSystemApi()
sysid = 'sysid_example' # str | sensor system id

try: 
    # Get a sensor system
    api_response = api_instance.get_system(sysid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorSystemApi->get_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sysid** | **str**| sensor system id | 

### Return type

[**SensorSystem**](SensorSystem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_systems**
> list[SensorSystemSummary] list_systems()

List all registered sensor systems



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SensorSystemApi()

try: 
    # List all registered sensor systems
    api_response = api_instance.list_systems()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorSystemApi->list_systems: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SensorSystemSummary]**](SensorSystemSummary.md)

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
api_instance = swagger_client.SensorSystemApi()
sysid = 'sysid_example' # str | sensor system id
body = swagger_client.DataStreamAdd() # DataStreamAdd | stream definition

try: 
    # Add a data stream
    api_response = api_instance.register_stream(sysid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorSystemApi->register_stream: %s\n" % e)
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

# **register_system**
> SensorSystemSummary register_system(body)

Register sensor system



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SensorSystemApi()
body = swagger_client.SensorSystemAdd() # SensorSystemAdd | sensor system definition

try: 
    # Register sensor system
    api_response = api_instance.register_system(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorSystemApi->register_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SensorSystemAdd**](SensorSystemAdd.md)| sensor system definition | 

### Return type

[**SensorSystemSummary**](SensorSystemSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_system**
> SensorSystemSummary update_system(sysid, body)

Update a sensor system



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SensorSystemApi()
sysid = 'sysid_example' # str | sensor system id
body = swagger_client.SensorSystemUpdate() # SensorSystemUpdate | Properties to update. All elements are optional.

try: 
    # Update a sensor system
    api_response = api_instance.update_system(sysid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorSystemApi->update_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sysid** | **str**| sensor system id | 
 **body** | [**SensorSystemUpdate**](SensorSystemUpdate.md)| Properties to update. All elements are optional. | 

### Return type

[**SensorSystemSummary**](SensorSystemSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

