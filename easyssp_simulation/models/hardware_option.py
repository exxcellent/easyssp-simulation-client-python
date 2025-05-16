from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Self

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt


class HardwareOption(BaseModel):
    """
    The available hardware configuration options for simulations.
    """
    identifier: StrictInt = Field(
        description="Defines the identifier of this hardware option to be used when starting a simulation.")
    cpu_cores: StrictFloat | StrictInt = Field(
        description="Defines the number of cores available for the simulation with this hardware option.",
        alias="cpuCores")
    ram_in_gb: StrictFloat | StrictInt = Field(
        description="Defines the size of the ram available for the simulation with this hardware option.",
        alias="ramInGb")
    credit_cost_per_minute: StrictInt = Field(
        description="Defines the credit cost per minute for this hardware option.", alias="creditCostPerMinute")
    __properties: ClassVar[list[str]] = ["identifier", "cpuCores", "ramInGb", "creditCostPerMinute"]

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
        """Create an instance of HardwareOption from a JSON string"""
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
        """Create an instance of HardwareOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "identifier": obj.get("identifier"),
            "cpuCores": obj.get("cpuCores"),
            "ramInGb": obj.get("ramInGb"),
            "creditCostPerMinute": obj.get("creditCostPerMinute")
        })
        return _obj
