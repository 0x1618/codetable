from typing import ClassVar, Optional

from .codes_storage import CodesStorage


class ConfigTemplate:
    EXPORT_TO: ClassVar[Optional[CodesStorage]]
