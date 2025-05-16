# Simulation

A created and started simulation.

## Properties

| Name           | Type                    | Description                                                                                                 | Notes      |
|----------------|-------------------------|-------------------------------------------------------------------------------------------------------------|------------|
| **id**         | **str**                 | The id of the simulation. Can be used for requesting the simulation again and for modifying the simulation. | [optional] |
| **name**       | **str**                 | The name of the simulation.                                                                                 | [optional] |
| **start_time** | **datetime**            | The date and time the simulation has been created and started.                                              | [optional] |
| **runs**       | [**List[Run]**](Run.md) | The different runs the Simulation consists of.                                                              | [optional] |

## Example

```python
from easyssp_simulation.models.simulation import Simulation

simulation_instance = Simulation(id='d7b2a04e-2a8d-4292-8238-128b82dd7919', name='Simulation 1', startTime=None,
                                 runs=[])
# print the JSON string representation of the object
print(simulation_instance.to_json())

# convert the object into a dict
simulation_dict = simulation_instance.to_dict()
# create an instance of Simulation from a dict
simulation_from_dict = Simulation.from_dict(simulation_dict)
```

[[Back to README]](../../README.md)


