from collections.abc import Mapping
from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class Code(Mapping):
    code: str
    msg: str

    def __getitem__(self, key: str):
        return asdict(self)[key]

    def __iter__(self):
        return iter(asdict(self))

    def __len__(self):
        return len(asdict(self))


def msg(message: str) -> Any:
    return message
