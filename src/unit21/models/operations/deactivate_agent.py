import dataclasses
from typing import Any, Optional


@dataclasses.dataclass
class DeactivateAgentPathParams:
    agent_email: str = dataclasses.field(metadata={'path_param': { 'field_name': 'agent_email', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeactivateAgentRequest:
    path_params: DeactivateAgentPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeactivateAgentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    agent_list: Optional[Any] = dataclasses.field(default=None)
    