from typing import Any, ClassVar

from .code import Code
from .types import CodeRegistry


class Codes:
    NAMESPACE: ClassVar[str]

    def __init_subclass__(cls) -> None:
        cls.check_subclass_configuration()

        cls.code_registry: CodeRegistry = cls.make_code_registry()
        cls.integrate_code_registry()

    @classmethod
    def make_code_registry(cls) -> CodeRegistry:
        code_registry: CodeRegistry = {}

        for variable_name in cls.__annotations__:
            if variable_name == "NAMESPACE":
                continue

            code: str = f"{cls.NAMESPACE}_{variable_name}".lower()

            variable_value: Any = getattr(cls, variable_name, None)

            if variable_value is None:
                code_registry[variable_name] = code
            elif isinstance(variable_value, str):
                code_registry[variable_name] = Code(
                    code=code, msg=variable_value
                )
            else:
                raise TypeError(
                    f"Unsupported value type for {variable_value}: {type(variable_value)}"
                )

        return code_registry

    @classmethod
    def integrate_code_registry(cls) -> None:
        if getattr(cls, 'code_registry', None) is None:
            raise ValueError(
                'Code registry not created. Use "cls.make_code_registry" method.'
            )

        for key, value in cls.code_registry.items():
            setattr(cls, key, value)

    @classmethod
    def check_subclass_configuration(cls) -> None:
        if getattr(cls, "NAMESPACE", None) is None:
            raise ValueError('Class attribute "NAMESPACE" is required.')
