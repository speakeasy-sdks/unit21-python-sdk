import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from typing import Any, Optional
from unit21 import utils


@dataclasses.dataclass
class UpdateEventPathParams:
    event_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'event_id', 'style': 'simple', 'explode': False }})
    org_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_name', 'style': 'simple', 'explode': False }})
    
class UpdateEventEventOptionsOptionsLinkedEntityEnum(str, Enum):
    SENDER = "sender"
    RECEIVER = "receiver"
    BOTH = "both"


@dataclass_json
@dataclasses.dataclass
class UpdateEventEventOptionsOptions:
    link_digital_data_to_entity: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('link_digital_data_to_entity') }})
    linked_entity: Optional[UpdateEventEventOptionsOptionsLinkedEntityEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('linked_entity') }})
    merge_custom_data: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('merge_custom_data') }})
    monitor: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('monitor') }})
    resolve_geoip: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('resolve_geoip') }})
    upsert_on_conflict: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('upsert_on_conflict') }})
    

@dataclass_json
@dataclasses.dataclass
class UpdateEventEventOptions:
    options: Optional[UpdateEventEventOptionsOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('options') }})
    

@dataclasses.dataclass
class UpdateEventRequest:
    path_params: UpdateEventPathParams = dataclasses.field()
    request: Optional[UpdateEventEventOptions] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class UpdateEventMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class UpdateEventResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    message_general_response: Optional[UpdateEventMessageGeneralResponse] = dataclasses.field(default=None)
    update_event_response: Optional[Any] = dataclasses.field(default=None)
    