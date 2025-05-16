# StartSimulationConfiguration

The configuration for the simulation runs.

## Properties

| Name     | Type                                                                            | Description                                                                                             | Notes |
|----------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-------|
| **name** | **str**                                                                         | Required. Specifies a name for the simulation.                                                          |       |
| **runs** | [**List[StartSimulationRunConfiguration]**](StartSimulationRunConfiguration.md) | Required, at least one. Specifies configurations for simulation runs to execute on the given .ssp-file. |       |

## Example

```python
from easyssp_simulation.models.start_simulation_configuration import StartSimulationConfiguration

start_simulation_configuration_instance = StartSimulationConfiguration.from_json("""
        {
          "name": "Simulation 2",
          "runs": [
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
            },
            {
              "name": "Run 2",
              "ssdFileName": "SystemStructure.ssd",
              "hardwareIdentifier": 10242048,
              "maxRunDurationInMinutes": 10,
              "start": 0,
              "step": 0.1,
              "stop": 10,
              "outputRate": 1,
              "targetType": "Windows32"
            }
          ]
        }""")
# print the JSON string representation of the object
print(start_simulation_configuration_instance)

# convert the object into a dict
start_simulation_configuration_dict = start_simulation_configuration_instance.to_dict()
# create an instance of StartSimulationConfiguration from a dict
start_simulation_configuration_from_dict = StartSimulationConfiguration.from_dict(start_simulation_configuration_dict)
```

[[Back to README]](../../README.md)


