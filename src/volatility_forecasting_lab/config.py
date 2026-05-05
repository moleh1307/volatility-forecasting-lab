from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class ProjectConfig:
    tickers: list[str]
    start_date: str
    validation_start: str
    annualization_days: int


def load_config(path: str | Path = "configs/project.yml") -> ProjectConfig:
    raw = yaml.safe_load(Path(path).read_text())
    return ProjectConfig(
        tickers=list(raw["data"]["tickers"]),
        start_date=str(raw["data"]["start_date"]),
        validation_start=str(raw["evaluation"]["validation_start"]),
        annualization_days=int(raw["evaluation"]["annualization_days"]),
    )


def write_yaml(path: str | Path, data: dict[str, Any]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(yaml.safe_dump(data, sort_keys=False))
