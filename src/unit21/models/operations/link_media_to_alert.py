import dataclasses
from typing import Any, Optional


@dataclasses.dataclass
class LinkMediaToAlertPathParams:
    unit21_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'unit21_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class LinkMediaToAlertRequest:
    path_params: LinkMediaToAlertPathParams = dataclasses.field()
    request: Optional[Any] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class LinkMediaToAlertResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[Any] = dataclasses.field(default=None)
    