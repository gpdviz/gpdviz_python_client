# swagger_client.SystemApi

All URIs are relative to *http://localhost:5050/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system**](SystemApi.md#delete_system) | **DELETE** /ss/{sysid} | Unregister a sensor system
[**get_system**](SystemApi.md#get_system) | **GET** /ss/{sysid} | Get a sensor system
[**list_systems**](SystemApi.md#list_systems) | **GET** /ss | List all registered sensor systems
[**register_stream**](SystemApi.md#register_stream) | **POST** /ss/{sysid} | Add a data stream
[**register_system**](SystemApi.md#register_system) | **POST** /ss | Register sensor system
[**update_system**](SystemApi.md#update_system) | **PUT** /ss/{sysid} | Update a sensor system


# **delete_system**
> SensorSystem delete_system(sysid)

Unregister a sensor system



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()
sysid = 'sysid_example' # str | sensor system id

try: 
    # Unregister a sensor system
    api_response = api_instance.delete_system(sysid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->delete_system: %s\n" % e)
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
api_instance = swagger_client.SystemApi()
sysid = 'sysid_example' # str | sensor system id

try: 
    # Get a sensor system
    api_response = api_instance.get_system(sysid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_system: %s\n" % e)
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
> list[float] list_systems()

List all registered sensor systems



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()

try: 
    # List all registered sensor systems
    api_response = api_instance.list_systems()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->list_systems: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[float]**

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
api_instance = swagger_client.SystemApi()
sysid = 'sysid_example' # str | sensor system id
body = swagger_client.StreamRegister() # StreamRegister | stream definition

try: 
    # Add a data stream
    api_response = api_instance.register_stream(sysid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->register_stream: %s\n" % e)
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

# **register_system**
> SensorSystem register_system(body)

Register sensor system



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()
body = swagger_client.SSRegister() # SSRegister | sensor system definition

try: 
    # Register sensor system
    api_response = api_instance.register_system(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->register_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SSRegister**](SSRegister.md)| sensor system definition | 

### Return type

[**SensorSystem**](SensorSystem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_system**
> SensorSystem update_system(sysid, body)

Update a sensor system



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()
sysid = 'sysid_example' # str | sensor system id
body = swagger_client.SSUpdate() # SSUpdate | Properties to update

try: 
    # Update a sensor system
    api_response = api_instance.update_system(sysid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->update_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sysid** | **str**| sensor system id | 
 **body** | [**SSUpdate**](SSUpdate.md)| Properties to update | 

### Return type

[**SensorSystem**](SensorSystem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

