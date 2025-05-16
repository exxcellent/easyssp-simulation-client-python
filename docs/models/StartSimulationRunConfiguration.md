# StartSimulationRunConfiguration

Required, at least one. Specifies configurations for simulation runs to execute on the given .ssp-file.

## Properties

| Name                            | Type      | Description                                                                                                                                         | Notes      |
|---------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| **name**                        | **str**   | Optional, specifies the name of the run. Defaults to &#39;Run &lt;Number&gt;&#39; when not specified.                                               | [optional] |
| **ssd_file_name**               | **str**   | Optional, specifies the name of the run. Defaults to &#39;SystemStructure.ssd&#39; when not specified.                                              | [optional] |
| **hardware_identifier**         | **int**   | Required. The identifier for the hardware environment this simulation will run in the cloud.                                                        | [optional] |
| **max_run_duration_in_minutes** | **int**   | Required. The maximum duration of the run in minutes. Will be used for calculating the credit costs of the run.                                     | [optional] |
| **stimuli_file_name**           | **str**   | Optional. Specifies the name of the stimuli file to use for this run. The stimuli file has to be present in the stimuli files given in the request. | [optional] |
| **start**                       | **float** | Required. The start parameter for the simulation.                                                                                                   | [optional] |
| **step**                        | **float** | Required. The step parameter for the simulation.                                                                                                    | [optional] |
| **stop**                        | **float** | Required. The stop parameter for the simulation.                                                                                                    | [optional] |
| **output_rate**                 | **float** | Optional. The output rate for the simulation.                                                                                                       | [optional] |
| **target_type**                 | **str**   | Required. Specifies the target operating system the simulation will run in.                                                                         |            |

## Example

```python
from easyssp_simulation.models.start_simulation_run_configuration import StartSimulationRunConfiguration

# create an instance of StartSimulationRunConfiguration from a JSON string
start_simulation_run_configuration_instance = StartSimulationRunConfiguration.from_json("""
{
  "name": "Run 1",
  "ssdFileName": "SystemStructure.ssd",
  "hardwareIdentifier": 10242048,
  "maxRunDurationInMinutes": 10,
  "start": 0,
  "step": 0.1,
  "stop": 10,
  "outputRate": 1,
  "targetType": "Windows32"
}""")
print(start_simulation_run_configuration_instance)

# convert the object into a dict
start_simulation_run_configuration_dict = start_simulation_run_configuration_instance.to_dict()
# create an instance of StartSimulationRunConfiguration from a dict
start_simulation_run_configuration_from_dict = StartSimulationRunConfiguration.from_dict(
    start_simulation_run_configuration_dict)
```

[[Back to README]](../../README.md)


