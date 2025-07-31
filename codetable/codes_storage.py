import json
from dataclasses import dataclass, field


@dataclass
class CodesStorage:
    storage: dict = field(init=False, default_factory=lambda: {})

    def update(self, extracted_codes: dict) -> None:
        for code in extracted_codes:
            if code in self.storage:
                raise ValueError(f"Duplicate code detected: {code}.")

        self.storage.update(extracted_codes)

    def to_json(self, indent: int = 4) -> str:
        return json.dumps(self.storage, indent=indent)

    def to_dict(self) -> dict:
        return self.storage
