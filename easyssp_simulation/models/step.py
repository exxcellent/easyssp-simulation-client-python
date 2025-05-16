from __future__ import annotations

from datetime import datetime
import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Self

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator


class Step(BaseModel):
    """
    Each simulation run is split into two steps. The 'generate' step will generate a simulator. The 'simulate' step will use that simulator to perform the simulation with the given configurations.
    """
    id: StrictStr = Field(description="The id of the simulation step. Can be used for requesting the logs of the step.")
    step_key: StrictStr = Field(
        description="Indicates the type of the step. The 'generate' step will generate a simulator. The 'simulate' step will use that simulator to perform the simulation with the given configurations.",
        alias="stepKey")
    step_status: StrictStr = Field(
        description="The current status of the step. Possible states are created (not yet started, possibly due to prior tasks), queued (The step is awaiting startup in the execution queue), start_pending (execution container is being build and provided), running, error, done (The step has finished in time), time_out (The step exceeded its time limit, and has been stopped), stop_pending (a manual stop has been issued and the stop is prepared), stopped (The step has been manually stopped).",
        alias="stepStatus")
    start_time: datetime | None = Field(default=None,
                                        description="Specifies the date and time when the step was started.",
                                        alias="startTime")
    end_time: datetime | None = Field(default=None,
                                      description="Specifies the date and time when the step was terminated (success or failure).",
                                      alias="endTime")
    __properties: ClassVar[list[str]] = ["id", "stepKey", "stepStatus", "startTime", "endTime"]

    @field_validator("step_key")
    def step_key_validate_enum(cls, value):
        """Validates the enum"""
        if value not in {"generate", "simulate"}:
            raise ValueError("must be one of enum values ('generate', 'simulate')")
        return value

    @field_validator("step_status")
    def step_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in {
            "created", "queued", "start_pending", "running", "error", "stop_pending", "stopped", "timed_out",
            "done"}:
            raise ValueError(
                "must be one of enum values ('created', 'queued', 'start_pending', 'running', 'error', 'stop_pending', 'stopped', 'timed_out', 'done')")
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
        """Create an instance of Step from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of Step from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "stepKey": obj.get("stepKey"),
            "stepStatus": obj.get("stepStatus"),
            "startTime": obj.get("startTime"),
            "endTime": obj.get("endTime")
        })
        return _obj
