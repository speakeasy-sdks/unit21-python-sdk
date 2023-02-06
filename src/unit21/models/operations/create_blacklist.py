import dataclasses
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclasses.dataclass
class CreateBlacklistRequest:
    request: Any = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class CreateBlacklistMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class CreateBlacklistResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_blacklist_response: Optional[Any] = dataclasses.field(default=None)
    message_general_response: Optional[CreateBlacklistMessageGeneralResponse] = dataclasses.field(default=None)
    