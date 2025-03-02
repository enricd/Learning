from datetime import datetime
from typing import Dict, Any, Optional, List
from pydantic import BaseModel
from pathlib import Path


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
        output_names = [Path(x).name for x in _output]
        files = []
        for x, output_path in enumerate(output_names):
            suffix = output_path.suffix
            files.append(f"{url}/file/{x}{suffix}")

        return cls(
            id=_id,
            url=url,
            model=data.get("model"),
            version=data.get("version"),
            created_at=data.get("created_at"),
            completed_at=data.get("completed_at"),
            files=files,
            num_outputs=num_outputs,
        )