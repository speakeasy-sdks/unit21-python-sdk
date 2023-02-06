import dataclasses
from typing import Any, Optional


@dataclasses.dataclass
class LinkMediaToEntityPathParams:
    entity_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'entity_id', 'style': 'simple', 'explode': False }})
    org_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_name', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class LinkMediaToEntityRequest:
    path_params: LinkMediaToEntityPathParams = dataclasses.field()
    request: Optional[Any] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class LinkMediaToEntityResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[Any] = dataclasses.field(default=None)
    