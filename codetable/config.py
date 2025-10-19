from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Optional

if TYPE_CHECKING:
    from contextvars import ContextVar

from .codes_storage import CodesStorage


class ConfigTemplate:
    EXPORT_TO: ClassVar[Optional[CodesStorage]]

    CURRENT_LANGUAGE: ClassVar[Optional[ContextVar[str]]]
    FALLBACK_LANGUAGE: ClassVar[Optional[str]]
