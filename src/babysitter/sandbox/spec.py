from enum import auto, Enum
from pathlib import Path
from dataclasses import dataclass


@dataclass
class MountSpec:
    source: Path
    target: Path


class NetworkPolicy(Enum):
    NONE = auto()
    HOST = auto()


@dataclass(slots=True)
class SandboxSpec:
    workdir: Path
    mounts: list[MountSpec]
    env: dict[str, str]
    network_policy: NetworkPolicy
