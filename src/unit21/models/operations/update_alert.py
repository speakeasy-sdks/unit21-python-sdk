import dataclasses
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclasses.dataclass
class UpdateAlertPathParams:
    unit21_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'unit21_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateAlertRequest:
    path_params: UpdateAlertPathParams = dataclasses.field()
    request: Optional[Any] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class UpdateAlertMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class UpdateAlertResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    message_general_response: Optional[UpdateAlertMessageGeneralResponse] = dataclasses.field(default=None)
    update_alert_response: Optional[Any] = dataclasses.field(default=None)
    