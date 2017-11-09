# swagger_client.ObservationApi

All URIs are relative to *http://localhost:5050/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_observations**](ObservationApi.md#add_observations) | **POST** /ss/{sysid}/{strid}/obs | Add observations


# **add_observations**
> ObservationsSummary add_observations(sysid, strid, body)

Add observations



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObservationApi()
sysid = 'sysid_example' # str | sensor system id
strid = 'strid_example' # str | data stream id
body = swagger_client.ObservationsAdd() # ObservationsAdd | The observations

try: 
    # Add observations
    api_response = api_instance.add_observations(sysid, strid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObservationApi->add_observations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sysid** | **str**| sensor system id | 
 **strid** | **str**| data stream id | 
 **body** | [**ObservationsAdd**](ObservationsAdd.md)| The observations | 

### Return type

[**ObservationsSummary**](ObservationsSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

