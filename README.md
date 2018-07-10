# swagger-client
The Gpdviz REST API deals with three main kinds of resources: sensor systems, data streams, and observations.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.4.5
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/gpdviz/gpdviz_python_client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/gpdviz/gpdviz_python_client.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *http://localhost:5050/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DataStreamApi* | [**delete_stream**](docs/DataStreamApi.md#delete_stream) | **DELETE** /ss/{sysid}/{strid} | Delete a data stream
*DataStreamApi* | [**get_stream**](docs/DataStreamApi.md#get_stream) | **GET** /ss/{sysid}/{strid} | Get a data stream
*DataStreamApi* | [**register_stream**](docs/DataStreamApi.md#register_stream) | **POST** /ss/{sysid} | Add a data stream
*ObservationApi* | [**add_observations**](docs/ObservationApi.md#add_observations) | **POST** /ss/{sysid}/{strid}/obs | Add observations
*SensorSystemApi* | [**delete_system**](docs/SensorSystemApi.md#delete_system) | **DELETE** /ss/{sysid} | Unregister a sensor system
*SensorSystemApi* | [**get_system**](docs/SensorSystemApi.md#get_system) | **GET** /ss/{sysid} | Get a sensor system
*SensorSystemApi* | [**list_systems**](docs/SensorSystemApi.md#list_systems) | **GET** /ss | List all registered sensor systems
*SensorSystemApi* | [**register_stream**](docs/SensorSystemApi.md#register_stream) | **POST** /ss/{sysid} | Add a data stream
*SensorSystemApi* | [**register_system**](docs/SensorSystemApi.md#register_system) | **POST** /ss | Register sensor system
*SensorSystemApi* | [**update_system**](docs/SensorSystemApi.md#update_system) | **PUT** /ss/{sysid} | Update a sensor system
*VariableDefinitionApi* | [**add_variable_def**](docs/VariableDefinitionApi.md#add_variable_def) | **POST** /ss/{sysid}/{strid}/vd | Add variable definition


## Documentation For Models

 - [DataStream](docs/DataStream.md)
 - [DataStreamAdd](docs/DataStreamAdd.md)
 - [DataStreamSummary](docs/DataStreamSummary.md)
 - [LatLon](docs/LatLon.md)
 - [ObsData](docs/ObsData.md)
 - [ObservationsAdd](docs/ObservationsAdd.md)
 - [ObservationsSummary](docs/ObservationsSummary.md)
 - [ScalarData](docs/ScalarData.md)
 - [SensorSystem](docs/SensorSystem.md)
 - [SensorSystemAdd](docs/SensorSystemAdd.md)
 - [SensorSystemSummary](docs/SensorSystemSummary.md)
 - [SensorSystemUpdate](docs/SensorSystemUpdate.md)
 - [VariableDef](docs/VariableDef.md)
 - [VariableDefSummary](docs/VariableDefSummary.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



