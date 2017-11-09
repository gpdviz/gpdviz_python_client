# swagger_client.VariableDefinitionApi

All URIs are relative to *http://localhost:5050/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_variable_def**](VariableDefinitionApi.md#add_variable_def) | **POST** /ss/{sysid}/{strid}/vd | Add variable definition


# **add_variable_def**
> VariableDefSummary add_variable_def(sysid, strid, body)

Add variable definition



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariableDefinitionApi()
sysid = 'sysid_example' # str | sensor system id
strid = 'strid_example' # str | data stream id
body = swagger_client.VariableDef() # VariableDef | The variable definition

try: 
    # Add variable definition
    api_response = api_instance.add_variable_def(sysid, strid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariableDefinitionApi->add_variable_def: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sysid** | **str**| sensor system id | 
 **strid** | **str**| data stream id | 
 **body** | [**VariableDef**](VariableDef.md)| The variable definition | 

### Return type

[**VariableDefSummary**](VariableDefSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

