import dataclasses
from typing import Any, Optional


@dataclasses.dataclass
class LinkMediaToCasePathParams:
    unit21_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'unit21_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class LinkMediaToCaseRequest:
    path_params: LinkMediaToCasePathParams = dataclasses.field()
    request: Optional[Any] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class LinkMediaToCaseResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[Any] = dataclasses.field(default=None)
    