from datetime import datetime
from typing import Dict, Any, Optional, List
from pydantic import BaseModel
from pathlib import Path


class PredictionCreateModel(BaseModel):
    id: str
    url: str
    status: str

    @classmethod
    def from_replicate(cls, data: Dict[str, Any]) -> "PredictionCreateModel":
        _id = data.get("id")
        url = f"/predictions/{_id}"

        return cls(
            id=_id,
            url=url,
            status=data.get("status"),
        )
    

class PredictionListModel(BaseModel):
    id: str
    url: str
    status: str
    created_at: datetime
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    @classmethod
    def from_replicate(cls, data: Dict[str, Any]) -> "PredictionListModel":
        _id = data.get("id")
        url = f"/predictions/{_id}"

        return cls(
            id=_id,
            url=url,
            created_at=data.get("created_at"),
            started_at=data.get("started_at"),
            completed_at=data.get("completed_at"),
            status=data.get("status"),
        )


class PredictionDetailModel(BaseModel):
    id: str
    url: str
    model: str
    version: str
    created_at: datetime
    completed_at: Optional[datetime] = None
    files: Optional[List[str]] = None
    num_outputs: Optional[int] = 0

    @classmethod
    def from_replicate(cls, data: Dict[str, Any]) -> "PredictionDetailModel":
        _id = data.get("id")
        url = f"/predictions/{_id}"
        _input = data.get("input")
        num_outputs = _input.get("num_outputs") or 0
        _output = data.get("output") or []
        output_names = [Path(x) for x in _output]
        files = []
        for idx, output_path in enumerate(output_names):
            suffix = output_path.suffix
            files.append(f"{url}/files/{idx}{suffix}")

        return cls(
            id=_id,
            url=url,
            model=data.get("model"),
            version=data.get("version"),
            created_at=data.get("created_at"),
            completed_at=data.get("completed_at"),
            files=files,
            status=data.get("status"),
            num_outputs=num_outputs,
        )