import dataclasses
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclasses.dataclass
class GetEventPathParams:
    event_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'event_id', 'style': 'simple', 'explode': False }})
    org_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_name', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetEventRequest:
    path_params: GetEventPathParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetEventMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class GetEventResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    event_list: Optional[Any] = dataclasses.field(default=None)
    message_general_response: Optional[GetEventMessageGeneralResponse] = dataclasses.field(default=None)
    