import dataclasses
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclasses.dataclass
class CreateEntityRequest:
    request: Optional[Any] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class CreateEntityMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class CreateEntityResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_entity_response: Optional[Any] = dataclasses.field(default=None)
    message_general_response: Optional[CreateEntityMessageGeneralResponse] = dataclasses.field(default=None)
    