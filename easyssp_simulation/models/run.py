from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Self

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictFloat,
    StrictInt,
    StrictStr,
    field_validator,
)

from easyssp_simulation.models.step import Step


class Run(BaseModel):
    """
    The different runs the Simulation consists of.
    """
    id: StrictStr = Field(
        description="The id of the simulation run. Can be used for requesting the results and for modifying the simulation run.")
    run_name: StrictStr = Field(description="The name of the simulation run.", alias="runName")
    ssd_file_name: StrictStr = Field(
        description="The file name of the system structure (.ssd-file) inside the .ssp-file the simulation was performed on for this run.",
        alias="ssdFileName")
    run_status: StrictStr = Field(
        description="The current status of the run. Is based on the status for each step. Possible states are created (not yet started, execution is being prepared), start_pending (The first step is in a start_pending state), running(the first step entered the running state, until error or last step finished), error (one step has an error), done (The last step is done), time_out (a step exceeded its time limit, and has been stopped), stop_pending (a manual stop has been issued and the stop is prepared) and stopped (a step has been manually stopped).",
        alias="runStatus")
    steps: list[Step] = Field(
        description="Each simulation run is split into two steps. The 'generate' step will generate a simulator. The 'simulate' step will use that simulator to perform the simulation with the given configurations.")
    start: StrictFloat | StrictInt = Field(
        description="The start value for the simulation in seconds.")
    step: StrictFloat | StrictInt = Field(
        description="The step size value for the simulation in seconds.")
    stop: StrictFloat | StrictInt = Field(
        description="The stop value for the simulation in seconds.")
    output_rate: StrictInt | None = Field(default=None,
                                          description="The output rate for the simulation output in number of steps to skip.",
                                          alias="outputRate")
    stimuli_file_name: StrictStr | None = Field(default=None,
                                                description="The file name of the stimuli to use/has been used for the simulation.",
                                                alias="stimuliFileName")
    target_type: StrictStr = Field(description="The target OS execution platform the simulation is executed on.",
                                   alias="targetType")
    max_run_duration_in_minutes: StrictInt = Field(
        description="The setting for the maximum allowed run duration for this run.", alias="maxRunDurationInMinutes")
    credit_cost: StrictInt = Field(description="The credit costs of this run.", alias="creditCost")
    credit_refund: StrictInt = Field(
        description="The credits that has been refunded after the run has been finished, due to unused run minutes that has been set by 'maxRunDurationInMinutes'.",
        alias="creditRefund")
    cpu_cores: StrictFloat | StrictInt = Field(description="The number of cpu cores the simulation can use.",
                                               alias="cpuCores")
    ram_in_gb: StrictFloat | StrictInt = Field(description="The RAM Size the simulation can use.", alias="ramInGb")
    has_results: StrictBool = Field(
        description="Indicates whether the simulation has results. Is false as long as the simulation is still runing and will only become true if the simulation produced a simulation result.",
        alias="hasResults")
    has_result_sample: StrictBool = Field(
        description="Indicates whether the simulation has a sample of the simulation results. Will be true once the 'simulate' step started to produce results, even during the simulation run.",
        alias="hasResultSample")
    __properties: ClassVar[list[str]] = ["id", "runName", "ssdFileName", "runStatus", "steps", "start", "step", "stop",
                                         "outputRate", "stimuliFileName", "targetType", "maxRunDurationInMinutes",
                                         "creditCost", "creditRefund", "cpuCores", "ramInGb", "hasResults",
                                         "hasResultSample"]

    @field_validator("run_status")
    def run_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in {"created", "start_pending", "running", "error", "stop_pending", "stopped", "timed_out",
                         "done"}:
            raise ValueError(
                "must be one of enum values ('created', 'start_pending', 'running', 'error', 'stop_pending', 'stopped', 'timed_out', 'done')")
        return value

    @field_validator("target_type")
    def target_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in {"Windows32", "Windows64", "Linux64", "Linux32"}:
            raise ValueError("must be one of enum values ('Windows32', 'Windows64', 'Linux64', 'Linux32')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict(), default=str)

    @classmethod
    def from_json(cls, json_str: str) -> Self | None:
        """Create an instance of Run from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with the value `None`
          are ignored.
        """
        excluded_fields: set[str] = set({})

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in steps (list)
        _items = []
        if self.steps:
            for _item_steps in self.steps:
                if _item_steps:
                    _items.append(_item_steps.to_dict())
            _dict["steps"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of Run from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "runName": obj.get("runName"),
            "ssdFileName": obj.get("ssdFileName"),
            "runStatus": obj.get("runStatus"),
            "steps": [Step.from_dict(_item) for _item in obj["steps"]] if obj.get("steps") is not None else None,
            "start": obj.get("start"),
            "step": obj.get("step"),
            "stop": obj.get("stop"),
            "outputRate": obj.get("outputRate"),
            "stimuliFileName": obj.get("stimuliFileName"),
            "targetType": obj.get("targetType"),
            "maxRunDurationInMinutes": obj.get("maxRunDurationInMinutes"),
            "creditCost": obj.get("creditCost"),
            "creditRefund": obj.get("creditRefund"),
            "cpuCores": obj.get("cpuCores"),
            "ramInGb": obj.get("ramInGb"),
            "hasResults": obj.get("hasResults"),
            "hasResultSample": obj.get("hasResultSample")
        })
        return _obj
