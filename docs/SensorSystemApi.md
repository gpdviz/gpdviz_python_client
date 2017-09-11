# swagger_client.SensorSystemApi

All URIs are relative to *http://localhost:5050/api/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ss**](SensorSystemApi.md#add_ss) | **POST** /ss | Register sensor system
[**add_str**](SensorSystemApi.md#add_str) | **POST** /ss/{sysid} | Add a stream
[**delete_ss**](SensorSystemApi.md#delete_ss) | **DELETE** /ss/{sysid} | Unregister a sensor system
[**get_ss**](SensorSystemApi.md#get_ss) | **GET** /ss/{sysid} | Get a sensor system
[**list_ss**](SensorSystemApi.md#list_ss) | **GET** /ss | List all registered sensor systems
[**update_ss**](SensorSystemApi.md#update_ss) | **PUT** /ss/{sysid} | Update a sensor system


# **add_ss**
> SensorSystem add_ss(body)

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
body = swagger_client.SSRegister() # SSRegister | sensor system definition

try: 
    # Register sensor system
    api_response = api_instance.add_ss(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorSystemApi->add_ss: %s\n" % e)
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

# **add_str**
> SensorSystem add_str(sysid, body)

Add a stream



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
body = swagger_client.StreamRegister() # StreamRegister | stream definition

try: 
    # Add a stream
    api_response = api_instance.add_str(sysid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorSystemApi->add_str: %s\n" % e)
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

# **delete_ss**
> SensorSystem delete_ss(sysid)

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
    api_response = api_instance.delete_ss(sysid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorSystemApi->delete_ss: %s\n" % e)
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

# **get_ss**
> SensorSystem get_ss(sysid)

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
    api_response = api_instance.get_ss(sysid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorSystemApi->get_ss: %s\n" % e)
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

# **list_ss**
> list[float] list_ss()

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
    api_response = api_instance.list_ss()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorSystemApi->list_ss: %s\n" % e)
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

# **update_ss**
> SensorSystem update_ss(sysid, body)

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
body = swagger_client.SSUpdate() # SSUpdate | Properties to update

try: 
    # Update a sensor system
    api_response = api_instance.update_ss(sysid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorSystemApi->update_ss: %s\n" % e)
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

