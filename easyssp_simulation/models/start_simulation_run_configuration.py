from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Annotated, Any, ClassVar, Self

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictFloat,
    StrictInt,
    StrictStr,
    field_validator,
)


class StartSimulationRunConfiguration(BaseModel):
    """
    Required, at least one. Specifies configurations for simulation runs to execute on the given .ssp-file.
    """
    name: StrictStr | None = Field(default=None,
                                   description="Optional, specifies the name of the run. Defaults to 'Run <Number>' when not specified.")
    ssd_file_name: StrictStr | None = Field(default=None,
                                            description="Optional, specifies the name of the run. Defaults to 'SystemStructure.ssd' when not specified.",
                                            alias="ssdFileName")
    hardware_identifier: StrictInt = Field(
        description="Required. The identifier for the hardware environment this simulation will run in the cloud.",
        alias="hardwareIdentifier")
    max_run_duration_in_minutes: Annotated[int, Field(le=99999, strict=True, ge=1)] = Field(
        description="Required. The maximum duration of the run in minutes. Will be used for calculating the credit costs of the run.",
        alias="maxRunDurationInMinutes")
    stimuli_file_name: StrictStr | None = Field(default=None,
                                                description="Optional. Specifies the name of the stimuli file to use for this run. The stimuli file has to be present in the stimuli files given in the request.",
                                                alias="stimuliFileName")
    start: StrictFloat | StrictInt = Field(description="Required. The start parameter for the simulation.")
    step: StrictFloat | StrictInt = Field(description="Required. The step parameter for the simulation.")
    stop: StrictFloat | StrictInt = Field(description="Required. The stop parameter for the simulation.")
    output_rate: StrictInt | None = Field(default=None, description="Optional. The output rate for the simulation.",
                                          alias="outputRate")
    target_type: StrictStr = Field(
        description="Required. Specifies the target operating system the simulation will run in.", alias="targetType")
    __properties: ClassVar[list[str]] = ["name", "ssdFileName", "hardwareIdentifier", "maxRunDurationInMinutes",
                                         "stimuliFileName", "start", "step", "stop", "outputRate", "targetType"]

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
        """Create an instance of StartSimulationRunConfiguration from a JSON string"""
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
        """Create an instance of StartSimulationRunConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "ssdFileName": obj.get("ssdFileName"),
            "hardwareIdentifier": obj.get("hardwareIdentifier"),
            "maxRunDurationInMinutes": obj.get("maxRunDurationInMinutes"),
            "stimuliFileName": obj.get("stimuliFileName"),
            "start": obj.get("start"),
            "step": obj.get("step"),
            "stop": obj.get("stop"),
            "outputRate": obj.get("outputRate"),
            "targetType": obj.get("targetType")
        })
        return _obj
