from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Optional, Type

if TYPE_CHECKING:
    from contextvars import ContextVar

    from codetable.codes import Codes

MsgI18n = dict[str, str]
MsgSource = str | MsgI18n


class Code(Mapping):
    def __init__(
        self, code: str, msg_source: MsgSource, codes: Type[Codes]
    ) -> None:
        self.code: str = code
        self.msg_source: MsgSource = msg_source

        self._codes: Type[Codes] = codes

    @property
    def msg(self) -> str:
        if isinstance(self.msg_source, dict):
            fallback_lang: Optional[str] = self._codes.FALLBACK_LANGUAGE

            current_lang: Optional[
                str
            ] = self._codes.CURRENT_LANGUAGE and self._codes.CURRENT_LANGUAGE.get(
                fallback_lang
            )

            if fallback_lang is None:
                raise ValueError(
                    'FALLBACK_LANGUAGE is not defined in the "Codes" class, but multiple languages were detected.'
                )

            localized: Optional[str] = None

            if current_lang:
                localized = self.msg_source.get(current_lang)

            if localized is None:
                localized = self.msg_source.get(fallback_lang)

            if localized is None:
                raise ValueError(
                    f"No localization found for code '{self.code}'. "
                    f"Tried languages: current='{current_lang}', fallback='{fallback_lang}'."
                )

            return localized

        return self.msg_source

    def __getitem__(self, key: str):
        return self[key]

    def __iter__(self):
        return iter(self)

    def __len__(self):
        return len(self)

    def __repr__(self) -> str:
        return f"Code({self.code})"


def msg(message: MsgSource) -> Any:
    return message
