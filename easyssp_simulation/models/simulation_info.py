from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Self

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator

from easyssp_simulation.models.hardware_option import HardwareOption


class SimulationInfo(BaseModel):
    """
    SimulationInfo
    """
    available_hardware: list[HardwareOption] = Field(
        description="The available hardware configuration options for simulations.", alias="availableHardware")
    available_target_types: list[StrictStr] = Field(
        description="The available target OS execution platforms for simulations.", alias="availableTargetTypes")
    simulation_credit_fix_cost: StrictInt = Field(description="The fix credit fix costs to start a simulation.",
                                                  alias="simulationCreditFixCost")
    current_credits: StrictInt = Field(description="The credit amount of the current user.", alias="currentCredits")
    __properties: ClassVar[list[str]] = ["availableHardware", "availableTargetTypes", "simulationCreditFixCost",
                                         "currentCredits"]

    @field_validator("available_target_types")
    def available_target_types_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in {"Windows32", "Windows64", "Linux64", "Linux32"}:
                raise ValueError("each list item must be one of ('Windows32', 'Windows64', 'Linux64', 'Linux32')")
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
        """Create an instance of SimulationInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in available_hardware (a list)
        _items = []
        if self.available_hardware:
            for _item_available_hardware in self.available_hardware:
                if _item_available_hardware:
                    _items.append(_item_available_hardware.to_dict())
            _dict["availableHardware"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of SimulationInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availableHardware": [HardwareOption.from_dict(_item) for _item in obj["availableHardware"]] if obj.get(
                "availableHardware") is not None else None,
            "availableTargetTypes": obj.get("availableTargetTypes"),
            "simulationCreditFixCost": obj.get("simulationCreditFixCost"),
            "currentCredits": obj.get("currentCredits")
        })
        return _obj
