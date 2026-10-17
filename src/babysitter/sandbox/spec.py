from enum import auto, Enum
from pathlib import Path
from dataclasses import dataclass


class MountAccess(Enum):
    READ_ONLY = auto()
    READ_WRITE = auto()


@dataclass
class MountSpec:
    source: Path
    target: Path
    access: MountAccess = MountAccess.READ_ONLY


class NetworkPolicy(Enum):
    NONE = auto()
    HOST = auto()


@dataclass(slots=True)
class SandboxSpec:
    workdir: Path
    mounts: list[MountSpec]
    env: dict[str, str]
    network_policy: NetworkPolicy
