# SimulationInfo

## Properties

| Name                           | Type                                          | Description                                                   | Notes      |
|--------------------------------|-----------------------------------------------|---------------------------------------------------------------|------------|
| **available_hardware**         | [**List[HardwareOption]**](HardwareOption.md) | The available hardware configuration options for simulations. | [optional] |
| **available_target_types**     | **List[str]**                                 | The available target OS execution platforms for simulations.  | [optional] |
| **simulation_credit_fix_cost** | **int**                                       | The fix credit fix costs to start a simulation.               | [optional] |
| **current_credits**            | **int**                                       | The credit amount of the current user.                        | [optional] |

## Example

```python
from easyssp_simulation.models.simulation_info import SimulationInfo

simulation_info_instance = SimulationInfo(availableHardware=[],
                                          availableTargetTypes=['Linux64', 'Windows64', 'Windows32', 'Linux32'],
                                          simulationCreditFixCost=100, currentCredits=1000)
# print the JSON string representation of the object
print(simulation_info_instance.to_json())

# convert the object into a dict
simulation_info_dict = simulation_info_instance.to_dict()
# create an instance of SimulationInfo from a dict
simulation_info_from_dict = SimulationInfo.from_dict(simulation_info_dict)
```

[[Back to README]](../../README.md)


