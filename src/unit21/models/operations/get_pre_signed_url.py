import dataclasses
from typing import Any, Optional


@dataclasses.dataclass
class GetPreSignedURLRequest:
    request: Optional[Any] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class GetPreSignedURLResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    