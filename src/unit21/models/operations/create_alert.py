import dataclasses
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclasses.dataclass
class CreateAlertRequest:
    request: Optional[Any] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class CreateAlertMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class CreateAlertResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_alert_response: Optional[Any] = dataclasses.field(default=None)
    message_general_response: Optional[CreateAlertMessageGeneralResponse] = dataclasses.field(default=None)
    