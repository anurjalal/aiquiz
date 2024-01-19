from dataclasses import dataclass, asdict


@dataclass
class CommonResponse:
    success: bool
    message: str

    @property
    def __dict__(self):
        return asdict(self)