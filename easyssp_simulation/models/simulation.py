from __future__ import annotations

from datetime import datetime
import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Self

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from easyssp_simulation.models.run import Run


class Simulation(BaseModel):
    """
    The created and started simulation.
    """
    id: StrictStr = Field(
        description="The id of the simulation. Can be used for requesting the simulation again and for modifying the simulation.")
    name: StrictStr = Field(description="The name of the simulation.")
    start_time: datetime | None = Field(default=None,
                                        description="The date and time the simulation has been created and started.",
                                        alias="startTime")
    runs: list[Run] = Field(description="The different runs the Simulation consists of.")
    __properties: ClassVar[list[str]] = ["id", "name", "startTime", "runs"]

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
        """Create an instance of Simulation from a JSON string"""
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
        """Create an instance of Simulation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "startTime": obj.get("startTime"),
            "runs": [Run.from_dict(_item) for _item in obj["runs"]] if obj.get("runs") is not None else None
        })
        return _obj
