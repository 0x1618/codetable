from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar, Optional

from .code import Code

if TYPE_CHECKING:
    from contextvars import ContextVar

    from .codes_storage import CodesStorage
    from .types import CodeRegistry

FORBIDDEN_VARIABLE_NAMES = (
    "NAMESPACE", "CURRENT_LANGUAGE", "FALLBACK_LANGUAGE", "EXPORT_TO"
)


class Codes:
    NAMESPACE: ClassVar[str]

    CURRENT_LANGUAGE: ClassVar[Optional[ContextVar[str]]] = None
    FALLBACK_LANGUAGE: ClassVar[Optional[str]] = None

    EXPORT_TO: ClassVar[Optional[CodesStorage]] = None

    def __init_subclass__(cls) -> None:
        cls.check_subclass_configuration()

        cls.code_registry: CodeRegistry = cls.make_code_registry()
        cls.integrate_code_registry()

        if getattr(cls, "EXPORT_TO", None):
            cls.export_codes()

    @classmethod
    def make_code_registry(cls) -> CodeRegistry:
        code_registry: CodeRegistry = {}

        for variable_name in cls.__annotations__:
            if variable_name in FORBIDDEN_VARIABLE_NAMES:
                continue

            code: str = f"{cls.NAMESPACE}_{variable_name}".lower()

            variable_value: Any = getattr(cls, variable_name, None)

            if variable_value is None:
                code_registry[variable_name] = code
            elif type(variable_value) in (str, dict):
                code_registry[variable_name] = Code(
                    code=code, msg_source=variable_value, codes=cls
                )
            else:
                raise TypeError(
                    f"Unsupported value type for {variable_value}: {type(variable_value)}"
                )

        return code_registry

    @classmethod
    def integrate_code_registry(cls) -> None:
        cls.check_code_registry_presence()

        for key, value in cls.code_registry.items():
            setattr(cls, key, value)

    @classmethod
    def check_subclass_configuration(cls) -> None:
        if getattr(cls, "NAMESPACE", None) is None:
            raise ValueError('Class attribute "NAMESPACE" is required.')

        if (getattr(cls, "CURRENT_LANGUAGE", None) is not None) and \
           (getattr(cls, "FALLBACK_LANGUAGE", None) is None):
            raise ValueError(
                'Class attribute "FALLBACK_LANGUAGE" is required when "CURRENT_LANGUAGE" is defined.'
            )

    @classmethod
    def check_code_registry_presence(cls) -> None:
        if getattr(cls, 'code_registry', None) is None:
            raise ValueError(
                'Code registry not created. Use "cls.make_code_registry" method.'
            )

    @classmethod
    def export_codes(cls) -> dict:
        cls.check_code_registry_presence()

        exported_codes: dict = {}

        for code in cls.code_registry.values():
            if isinstance(code, str):
                exported_codes[code] = None
            elif isinstance(code, Code):
                exported_codes[code.code] = code.msg_source
            else:
                raise TypeError(
                    f"Unsupported value type for {code}: {type(code)}"
                )

        if cls.EXPORT_TO is not None:
            cls.EXPORT_TO.update(exported_codes)

        return exported_codes
