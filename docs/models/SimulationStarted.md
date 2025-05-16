# SimulationStarted

## Properties

| Name                  | Type                            | Description                                     | Notes      |
|-----------------------|---------------------------------|-------------------------------------------------|------------|
| **simulation**        | [**Simulation**](Simulation.md) |                                                 | [optional] |
| **total_credit_cost** | **int**                         | The total credit costs for this simulation.     | [optional] |
| **remaining_credits** | **int**                         | The remaining credits for the user.             | [optional] |
| **url**               | **str**                         | The url to access the simulations for the user. | [optional] |

## Example

```python
from easyssp_simulation.models.simulation_started import SimulationStarted

# create an instance of SimulationStarted from a JSON string
simulation_started_instance = SimulationStarted.from_json("""
{
  "simulation": {
    "id": "2b351933-1a65-4d3a-9bd5-d08fb55b757e",
    "name": "Simulation 2",
    "startTime": "2025-04-09 15:20:06.042000+00:00",
    "runs": [
      {
        "id": "b4b8a308-67a6-4233-a93c-b29fd7a5ac8f",
        "runName": "Run 1",
        "ssdFileName": "SystemStructure.ssd",
        "runStatus": "start_pending",
        "steps": [
          {
            "id": "35a4ba06-7972-4410-85f9-17e0e12ee9d3",
            "stepKey": "generate",
            "stepStatus": "queued"
          },
          {
            "id": "71b6449c-f5ef-437f-abbd-2666e5dd81a1",
            "stepKey": "simulate",
            "stepStatus": "created"
          }
        ],
        "start": 0,
        "step": 0.1,
        "stop": 10,
        "targetType": "Windows32",
        "maxRunDurationInMinutes": 10,
        "creditCost": 300,
        "creditRefund": 0,
        "cpuCores": 1,
        "ramInGb": 2,
        "hasResults": false,
        "hasResultSample": false
      },
      {
        "id": "1d515c61-0963-41c3-94dd-411face8186d",
        "runName": "Run 2",
        "ssdFileName": "SystemStructure.ssd",
        "runStatus": "start_pending",
        "steps": [
          {
            "id": "bcb16748-3e96-4f24-8273-3a896a29966c",
            "stepKey": "generate",
            "stepStatus": "queued"
          },
          {
            "id": "b2925e79-8d15-43ad-9618-2f2d8d47de75",
            "stepKey": "simulate",
            "stepStatus": "created"
          }
        ],
        "start": 0,
        "step": 0.1,
        "stop": 10,
        "targetType": "Windows32",
        "maxRunDurationInMinutes": 10,
        "creditCost": 300,
        "creditRefund": 0,
        "cpuCores": 1,
        "ramInGb": 2,
        "hasResults": false,
        "hasResultSample": false
      }
    ]
  },
  "totalCreditCost": -600,
  "remainingCredits": 67700,
  "url": "https://www.easy-ssp.com/app/#/simulation-api"
}""")
print(simulation_started_instance)

# convert the object into a dict
simulation_started_dict = simulation_started_instance.to_dict()
# create an instance of SimulationStarted from a dict
simulation_started_from_dict = SimulationStarted.from_dict(simulation_started_dict)
```

[[Back to README]](../../README.md)


