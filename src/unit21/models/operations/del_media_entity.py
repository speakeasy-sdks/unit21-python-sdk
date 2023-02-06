import dataclasses
from typing import Any, Optional


@dataclasses.dataclass
class DelMediaEntityPathParams:
    entity_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'entity_id', 'style': 'simple', 'explode': False }})
    org_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_name', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DelMediaEntityRequest:
    path_params: DelMediaEntityPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DelMediaEntityResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[Any] = dataclasses.field(default=None)
    