# [Simulation Client](../../easyssp_simulation/client/simulation_client.py)

All URIs are relative to *https://www.easy-ssp.com*

| Method                                                                               | HTTP request                                                     | Description                                       |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------|---------------------------------------------------|
| [**get_simulation**](SimulationClient.md#get_simulation)                             | **GET** /integration/api/v1/simulation/{simulationId}            | Request the simulation with the given id.         |
| [**get_simulations**](SimulationClient.md#get_simulations)                           | **GET** /integration/api/v1/simulation                           | Request all available simulations.                |
| [**delete_simulation**](SimulationClient.md#delete_simulation)                       | **DELETE** /integration/api/v1/simulation/{simulationId}         | Deletes the given simulation.                     |
| [**delete_simulation_run**](SimulationClient.md#delete_simulation_run)               | **DELETE** /integration/api/v1/simulation/run/{runId}            | Deletes the given simulation run.                 |
| [**get_simulation_result_sample**](SimulationClient.md#get_simulation_result_sample) | **GET** /integration/api/v1/simulation/run/{runId}/result/sample | Request the sampled results of a simulation run.  |
| [**simulation_info**](SimulationClient.md#simulation_info)                           | **GET** /integration/api/v1/simulation/info                      | Receive Available Credits and Simulation Options. |
| [**get_simulation_log**](SimulationClient.md#get_simulation_log)                     | **GET** /integration/api/v1/simulation/step/{stepId}/log         | Request the log of a simulation step.             |
| [**get_simulation_result**](SimulationClient.md#get_simulation_result)               | **GET** /integration/api/v1/simulation/run/{runId}/result        | Request the results of a simulation run.          |
| [**start_simulation**](SimulationClient.md#start_simulation)                         | **POST** /integration/api/v1/simulation                          | Starts a simulation for a given SSP.              |
| [**stop_simulation**](SimulationClient.md#stop_simulation)                           | **POST** /integration/api/v1/simulation/{simulationId}/stop      | Stops the given simulation.                       |
| [**stop_simulation_run**](SimulationClient.md#stop_simulation_run)                   | **POST** /integration/api/v1/simulation/run/{runId}/stop         | Stops the given simulation run.                   |

# **get_simulation**

Request the simulation with the given id.

Returns a general overview of the simulation with the given id. Gives insight to the configuration and status for each
run and for each simulation step inside the runs. Also includes the ids of runs and steps to make further requests.

### Parameters

| Name              | Type    | Description                                               | Notes |
|-------------------|---------|-----------------------------------------------------------|-------|
| **simulation_id** | **str** | The id of the simulation started with the Simulation-API. |       |

### Return data type

[**Simulation**](../models/Simulation.md)

### Authorization

No authorization required (api_client is already authenticated)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                                               | Response headers |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| **200**     | The requested simulation is returned.                                                                                                                                                                     | -                |
| **404**     | There is no simulation associated with the given id or the id is invalid.                                                                                                                                 | -                |
| **500**     | A different error occurred while fetching the required simulation. This is usually an issue on our end. Please try again at a later time. If this issue persists, please contact us.                      | -                |
| **401**     | The request lacks a valid access token.                                                                                                                                                                   | -                |
| **403**     | - The user lacks the permissions to access the resource.<br/> - The user lacks permission to access the simulation.<br/> - The requested simulation was not created using the simulation integration api. | -                |

[[Back to README]](../../README.md)

# **get_simulations**

Request all available simulations.

Returns all simulations of the current user. Gives insight to the configuration and status for each run and for each
simulation step inside the runs. Also includes the ids of runs and steps to make further requests.

### Parameters

This endpoint does not need any parameter.

### Return data type

[**List[Simulation]**](../models/Simulation.md)

### Authorization

No authorization required (api_client is already authenticated)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                           | Response headers |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| **200**     | All simulations of the current user are returned.                                                                                                                                     | -                |
| **500**     | A different error occurred while fetching the required simulations. This is usually an issue on our end. Please try again at a later time. If this issue persists, please contact us. | -                |
| **401**     | The request lacks a valid access token.                                                                                                                                               | -                |
| **403**     | The user lacks the permissions to access the resource.                                                                                                                                | -                |

[[Back to README]](../../README.md)

# **delete_simulation**

Deletes the given simulation.

Deletes the simulation with the given id and all its runs with all associated data (Logs, Results, Configuration,
Status). A simulation can only be deleted if all simulation runs are finished (done, time_out, stopped or error state).

### Parameters

| Name              | Type    | Description                                               | Notes |
|-------------------|---------|-----------------------------------------------------------|-------|
| **simulation_id** | **str** | The id of the simulation started with the Simulation-API. |       |

### Return data type

void (empty response body)

### Authorization

No authorization required (api_client is already authenticated)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                                               | Response headers |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| **204**     | The simulation was successfully deleted.                                                                                                                                                                  | -                |
| **400**     | The simulation contains simulation runs, that are not yet finished.                                                                                                                                       | -                |
| **404**     | There is no simulation associated with the given id or the id is invalid.                                                                                                                                 | -                |
| **500**     | A different error occurred while deleting the simulation. This is usually an issue on our end. Please try again at a later time. If this issue persists, please contact us.                               | -                |
| **401**     | The request lacks a valid access token.                                                                                                                                                                   | -                |
| **403**     | - The user lacks the permissions to access the resource.<br/> - The user lacks permission to access the simulation.<br/> - The requested simulation was not created using the simulation integration api. | -                |

[[Back to README]](../../README.md)

# **delete_simulation_run**

Deletes the given simulation run.

Deletes the simulation run with the given id with all associated data (Logs, Results, Configuration, Status). If the
simulation run was the only run in the simulation, the simulation is deleted as well. A simulation run can only be
deleted if the run is finished (done, time_out, stopped or error state).

### Parameters

| Name       | Type    | Description                   | Notes |
|------------|---------|-------------------------------|-------|
| **run_id** | **str** | The id of the simulation run. |       |

### Return data type

void (empty response body)

### Authorization

No authorization required (api_client is already authenticated)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                                               | Response headers |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| **204**     | The simulation run was successfully deleted.                                                                                                                                                              | -                |
| **400**     | The simulation run is not yet finished.                                                                                                                                                                   | -                |
| **404**     | There is no simulation run associated with the given id or the id is invalid.                                                                                                                             | -                |
| **500**     | A different error occurred while deleting the simulation run. This is usually an issue on our end. Please try again at a later time. If this issue persists, please contact us.                           | -                |
| **401**     | The request lacks a valid access token.                                                                                                                                                                   | -                |
| **403**     | - The user lacks the permissions to access the resource.<br/> - The user lacks permission to access the simulation.<br/> - The requested simulation was not created using the simulation integration api. | -                |

[[Back to README]](../../README.md)

# **get_simulation_result_sample**

Requests the sampled results of a simulation run.

Delivers the results of a simulation run with the given id in a reduced size. Can be used to fetch the current results
during a ***running*** simulation, or to get a reduced preview of the results for performance purposes. The sample size
is limited to 10000 data points. Each data point is evenly distributed across all currently simulated data points,
representing a sup sampling of the actual results.

### Parameters

| Name       | Type    | Description                   | Notes |
|------------|---------|-------------------------------|-------|
| **run_id** | **str** | The id of the simulation run. |       |

### Return data type

**bytearray**

### Authorization

No authorization required (api_client is already authenticated)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/csv

### HTTP response details

| Status code | Description                                                                                                                                                                                               | Response headers |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| **200**     | The requested sampled result file is returned.                                                                                                                                                            | -                |
| **404**     | - There is no simulation run associated with the given id or the id is invalid.<br/> - The results has not been generated yet or there are no results, depending on the step status inside the run.       | -                |
| **500**     | A different error occurred while fetching the required simulation result. This is usually an issue on our end. Please try again at a later time. If this issue persists, please contact us.               | -                |
| **401**     | The request lacks a valid access token.                                                                                                                                                                   | -                |
| **403**     | - The user lacks the permissions to access the resource.<br/> - The user lacks permission to access the simulation.<br/> - The requested simulation was not created using the simulation integration api. | -                |

[[Back to README]](../../README.md)

# **simulation_info**

Receive Available Credits and Simulation Options.

Returns various general information required to interact with this API:

- A list of currently available hardware configurations, with their identifier, credit cost per minute and actually
  hardware sizes
- A list of available target execution platforms to run the simulation in.
- The current credit amount the user has.
- The general fix costs of a simulation.

### Parameters

This endpoint does not need any parameter.

### Return data type

[**SimulationInfo**](../models/SimulationInfo.md)

### Authorization

No authorization required (api_client is already authenticated)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                           | Response headers |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| **200**     | The required information is successfully returned.                                                                                                                                    | -                |
| **500**     | A different error occurred while fetching the required information. This is usually an issue on our end. Please try again at a later time. If this issue persists, please contact us. | -                |
| **401**     | The request lacks a valid access token.                                                                                                                                               | -                |
| **403**     | The user lacks the permissions to access the resource.                                                                                                                                | -                |

[[Back to README]](../../README.md)

# **get_simulation_log**

Request the log of a simulation step.

Delivers the simulation log output created by the step.

### Parameters

| Name        | Type    | Description                    | Notes |
|-------------|---------|--------------------------------|-------|
| **step_id** | **str** | The id of the simulation step. |       |

### Return data type

**bytearray**

### Authorization

No authorization required (api_client is already authenticated)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

### HTTP response details

| Status code | Description                                                                                                                                                                                                                  | Response headers |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| **200**     | The requested simulation log is returned as a file.                                                                                                                                                                          | -                |
| **404**     | - There is no simulation step associated with the given id or the id is invalid.<br/> - The log has not been generated yet or does not exist. A log is created once the step is no longer in created or start_pending state. | -                |
| **500**     | A different error occurred while fetching the required simulation step log. This is usually an issue on our end. Please try again at a later time. If this issue persists, please contact us.                                | -                |
| **401**     | The request lacks a valid access token.                                                                                                                                                                                      | -                |
| **403**     | - The user lacks the permissions to access the resource.<br/> - The user lacks permission to access the simulation.<br/> - The requested simulation was not created using the simulation integration api.                    | -                |

[[Back to README]](../../README.md)

# **get_simulation_result**

Request the results of a simulation run.

Delivers the final results of a ***finished*** simulation run with the given id. The results can only be requested once
the simulation is finished and will have the full resolution of all data points.

### Parameters

| Name       | Type    | Description                   | Notes |
|------------|---------|-------------------------------|-------|
| **run_id** | **str** | The id of the simulation run. |       |

### Return data type

**bytearray**

### Authorization

No authorization required (api_client is already authenticated)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/csv

### HTTP response details

| Status code | Description                                                                                                                                                                                                    | Response headers |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| **200**     | The requested result file is returned.                                                                                                                                                                         | -                |
| **404**     | - There is no simulation run associated with the given id or the id is invalid.<br/> - The results has not been generated yet or there are no results, depending on whether the run has finished successfully. | -                |
| **500**     | A different error occurred while fetching the required simulation result. This is usually an issue on our end. Please try again at a later time. If this issue persists, please contact us.                    | -                |
| **401**     | The request lacks a valid access token.                                                                                                                                                                        | -                |
| **403**     | - The user lacks the permissions to access the resource.<br/> - The user lacks permission to access the simulation.<br/> - The requested simulation was not created using the simulation integration api.      | -                |

[[Back to README]](../../README.md)

# **start_simulation**

Starts a simulation for a given SSP.

Starts a simulation for the given .ssp-file with included FMI 2.0 components. The request is a Multipart-Upload with the
following components:

- configuration: A Json-Object specifying the configuration of the simulation
    - name: The required name of the simulation
    - runs: The configuration for each simulation run. You can start multiple simulations on the given .ssp-file with
      different configurations.
        - name: Optional, Defaults to 'Run <Index-Number>'
        - ssdFileName: Optional, Defaults to 'SystemStructure.ssd.' Allows specifying simulations on different
          .ssd-files inside the .ssp-file.
        - hardwareIdentifier: A valid identifier for the hardware to use. You can request available hardware and their
          credit costs via the "/simulation/info"-Endpoint.
        - maxRunDurationInMinutes: The maximum allowed simulation duration for this run in minutes. Is required to debit
          credits per hardware configuration. If the simulation finishes early, the credits will be refunded
          accordingly.
        - stimuliFileName: Optional, specify the filename of the stimuli to use for this simulation run. Requires the
          specified file to be present in the 'stimuli' part of the request.
        - start: The starting 'time'-value for the simulation.
        - step: The step size of the 'time'-value for the simulation.
        - stop: The stop 'time'-value for the simulation.
        - outputRate: Optional, specifies every x-th step for output. Default is 1.
        - targetType: The target execution platform for the simulation to run in. This usually depends on the included
          FMI 2.0 components. You can request supported target execution platforms via the "/simulation/info"-Endpoint.
- ssp: The .ssp-file to simulate with.
- stimuli: Optional, any number of .csv-files to stimulate the different runs with. Files that are not referenced in a
  run will be ignored.

When successful, the API returns the status model for the created simulation, the remaining credits of the user and a
URL that can be used to open the simulation view of easySSP. Note that we do not validate the given ssp files nor the
stimuli beforehand.

### Parameters

| Name              | Type                                                                          | Description                                                                                                     | Notes      |
|-------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|------------|
| **configuration** | [**StartSimulationConfiguration**](../models/StartSimulationConfiguration.md) |                                                                                                                 |            |
| **ssp_file**      | **bytearray**                                                                 | The ssp file to simulate.                                                                                       |            |
| **stimuli_file**  | **List[bytearray]**                                                           | Optional Stimuli-Files to be used by the defined simulation runs. Each stimuli Needs to be referenced by a run. | [optional] |

### Return data type

[**SimulationStarted**](../models/SimulationStarted.md)

### Authorization

No authorization required (api_client is already authenticated)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 | Response headers |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| **200**     | The simulation has been queued successfully. Response entity contains a detailed overview of the created simulation and its runs. Includes the required ids for follow-up requests for the simulation. Use the id of the simulation to see updates to the simulation status, use the ids of the runs to request results and perform operations like stop and delete on the run, and the step id to requests the detailed logs of each step. | -                |
| **400**     | - The ssp file exceeds the allowed size (currently 500MB)<br/> - The stimuli file exceeds the allowed size (currently 1000MB)<br/> - The configuration is faulty, for example referencing a stimuli in a run, that was not given in the request. <br/>- Hardware identifier or target type does not exist.<br/> - Other validation issues...                                                                                                | -                |
| **500**     | A different error occurred while starting the simulation. This is usually an issue on our end. Please try again at a later time. If this issue persists, please contact us.                                                                                                                                                                                                                                                                 | -                |
| **401**     | The request lacks a valid access token.                                                                                                                                                                                                                                                                                                                                                                                                     | -                |
| **417**     | The user has insufficient credits available to start a simulation with the given configuration.                                                                                                                                                                                                                                                                                                                                             | -                |
| **403**     | The user lacks the permissions to access the resource.                                                                                                                                                                                                                                                                                                                                                                                      | -                |

[[Back to README]](../../README.md)

# **stop_simulation**

Stops the given simulation.

Requests to stop the simulation with the given id by setting all its runs to a stop_pending state. It may take a while
for the infrastructure to react and actually stop the simulations.

### Parameters

| Name              | Type    | Description                                               | Notes |
|-------------------|---------|-----------------------------------------------------------|-------|
| **simulation_id** | **str** | The id of the simulation started with the Simulation-API. |       |

### Return data type

void (empty response body)

### Authorization

No authorization required (api_client is already authenticated)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                                               | Response headers |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| **204**     | The stop has been issued.                                                                                                                                                                                 | -                |
| **404**     | There is no simulation associated with the given id or the id is invalid.                                                                                                                                 | -                |
| **500**     | A different error occurred while stopping the simulation. This is usually an issue on our end. Please try again at a later time. If this issue persists, please contact us.                               | -                |
| **401**     | The request lacks a valid access token.                                                                                                                                                                   | -                |
| **403**     | - The user lacks the permissions to access the resource.<br/> - The user lacks permission to access the simulation.<br/> - The requested simulation was not created using the simulation integration api. | -                |

[[Back to README]](../../README.md)

# **stop_simulation_run**

Stops the given simulation run.

Requests to stop the simulation run with the given id. The run status will change to stop_pending.It may take a while
for the infrastructure to react.

### Parameters

| Name       | Type    | Description                   | Notes |
|------------|---------|-------------------------------|-------|
| **run_id** | **str** | The id of the simulation run. |       |

### Return data type

void (empty response body)

### Authorization

No authorization required (api_client is already authenticated)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                                               | Response headers |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| **204**     | The stop has been issued.                                                                                                                                                                                 | -                |
| **404**     | There is no simulation run associated with the given id or the id is invalid.                                                                                                                             | -                |
| **500**     | A different error occurred while stopping the simulation run. This is usually an issue on our end. Please try again at a later time. If this issue persists, please contact us.                           | -                |
| **401**     | The request lacks a valid access token.                                                                                                                                                                   | -                |
| **403**     | - The user lacks the permissions to access the resource.<br/> - The user lacks permission to access the simulation.<br/> - The requested simulation was not created using the simulation integration api. | -                |

[[Back to README]](../../README.md)

