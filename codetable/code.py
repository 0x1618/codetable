from dataclasses import dataclass
from typing import Any, Optional


@dataclass(frozen=True)
class Code:
    code: str
    msg: Optional[str] = None


def msg(message: str) -> Any:
    return message
