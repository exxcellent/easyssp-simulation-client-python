# Step

Each simulation run is split into two steps. The 'generate' step will generate a simulator. The 'simulate' step will use
that simulator to perform the simulation with the given configurations.

## Properties

| Name            | Type         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Notes      |
|-----------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| **id**          | **str**      | The id of the simulation step. Can be used for requesting the logs of the step.                                                                                                                                                                                                                                                                                                                                                                                                          | [optional] |
| **step_key**    | **str**      | Indicates the type of the step. The &#39;generate&#39; step will generate a simulator. The &#39;simulate&#39; step will use that simulator to perform the simulation with the given configurations.                                                                                                                                                                                                                                                                                      | [optional] |
| **step_status** | **str**      | The current status of the step. Possible states are created (not yet started, possibly due to prior tasks), queued (The step is awaiting startup in the execution queue), start_pending (execution container is being build and provided), running, error, done (The step has finished in time), time_out (The step exceeded its time limit, and has been stopped), stop_pending (a manual stop has been issued and the stop is prepared), stopped (The step has been manually stopped). | [optional] |
| **start_time**  | **datetime** | Specifies the date and time when the step was started.                                                                                                                                                                                                                                                                                                                                                                                                                                   | [optional] |
| **end_time**    | **datetime** | Specifies the date and time when the step was terminated (success or failure).                                                                                                                                                                                                                                                                                                                                                                                                           | [optional] |

## Example

```python
from easyssp_simulation.models.step import Step

# create an instance of Step from a JSON string
step_instance = Step.from_json("""
{
    "id": "35a4ba06-7972-4410-85f9-17e0e12ee9d3",
    "stepKey": "generate",
    "stepStatus": "queued"
    "startTime": "2025-04-09 15:20:06.042000+00:00",
    "endTime": "2025-04-09 15:30:06.042000+00:00"
}""")
# print the JSON string representation of the object
print(step_instance)

# convert the object into a dict
step_dict = step_instance.to_dict()
# create an instance of Step from a dict
step_from_dict = Step.from_dict(step_dict)
```

[[Back to README]](../../README.md)


