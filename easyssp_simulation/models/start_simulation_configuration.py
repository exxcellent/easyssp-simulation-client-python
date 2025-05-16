from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Annotated, Any, ClassVar, Self

from pydantic import BaseModel, ConfigDict, Field

from easyssp_simulation.models.start_simulation_run_configuration import (
    StartSimulationRunConfiguration,
)


class StartSimulationConfiguration(BaseModel):
    """
    The configuration for the simulation runs.
    """
    name: Annotated[str, Field(min_length=0, strict=True, max_length=255)] = Field(
        description="Required. Specifies a name for the simulation.")
    runs: list[StartSimulationRunConfiguration] = Field(
        description="Required, at least one. Specifies configurations for simulation runs to execute on the given .ssp-file.")
    __properties: ClassVar[list[str]] = ["name", "runs"]

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
        """Create an instance of StartSimulationConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in runs (list)
        _items = []
        if self.runs:
            for _item_runs in self.runs:
                if _item_runs:
                    _items.append(_item_runs.to_dict())
            _dict["runs"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of StartSimulationConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "runs": [StartSimulationRunConfiguration.from_dict(_item) for _item in obj["runs"]] if obj.get(
                "runs") is not None else None
        })
        return _obj
