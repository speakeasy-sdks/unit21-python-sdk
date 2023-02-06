import dataclasses
from typing import Any, Optional


@dataclasses.dataclass
class ListAgentsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_agent_response: Optional[list[Any]] = dataclasses.field(default=None)
    