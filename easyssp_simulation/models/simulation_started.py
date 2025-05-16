from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Self

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr

from easyssp_simulation.models.simulation import Simulation


class SimulationStarted(BaseModel):
    """
    SimulationStarted
    """
    simulation: Simulation
    total_credit_cost: StrictInt = Field(description="The total credit costs for this simulation.",
                                         alias="totalCreditCost")
    remaining_credits: StrictInt = Field(description="The remaining credits for the user.", alias="remainingCredits")
    url: StrictStr = Field(description="The url to access the simulations for the user.")
    __properties: ClassVar[list[str]] = ["simulation", "totalCreditCost", "remainingCredits", "url"]

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
        """Create an instance of SimulationStarted from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of simulation
        if self.simulation:
            _dict["simulation"] = self.simulation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of SimulationStarted from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "simulation": Simulation.from_dict(obj["simulation"]) if obj.get("simulation") is not None else None,
            "totalCreditCost": obj.get("totalCreditCost"),
            "remainingCredits": obj.get("remainingCredits"),
            "url": obj.get("url")
        })
        return _obj
