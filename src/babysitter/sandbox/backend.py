from collections.abc import Sequence
from dataclasses import dataclass
from typing import Protocol

from .spec import SandboxSpec


@dataclass(frozen=True, slots=True)
class SandboxResult:
    returncode: int
    stdout: str
    stderr: str


class SandboxBackend(Protocol):
    async def run(self, spec: SandboxSpec, command: Sequence[str]) -> SandboxResult: ...
