# HardwareOption

The available hardware configuration options for simulations.

## Properties

| Name                       | Type      | Description                                                                           | Notes      |
|----------------------------|-----------|---------------------------------------------------------------------------------------|------------|
| **identifier**             | **int**   | Defines the identifier of this hardware option to be used when starting a simulation. | [optional] |
| **cpu_cores**              | **float** | Defines the number of cores available for the simulation with this hardware option.   | [optional] |
| **ram_in_gb**              | **float** | Defines the size of the ram available for the simulation with this hardware option.   | [optional] |
| **credit_cost_per_minute** | **int**   | Defines the credit cost per minute for this hardware option.                          | [optional] |

## Example

```python
from easyssp_simulation.models.hardware_option import HardwareOption

hardware_option_instance = HardwareOption(identifier=123, cpuCores=4, ramInGb=64, creditCostPerMinute=10)
# print the JSON string representation of the object
print(hardware_option_instance.to_json())

# convert the object into a dict
hardware_option_dict = hardware_option_instance.to_dict()
# create an instance of HardwareOption from a dict
hardware_option_from_dict = HardwareOption.from_dict(hardware_option_dict)
```

[[Back to README]](../../README.md)


