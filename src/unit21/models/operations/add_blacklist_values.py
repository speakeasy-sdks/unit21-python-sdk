import dataclasses
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclasses.dataclass
class AddBlacklistValuesPathParams:
    unit21_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'unit21_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AddBlacklistValuesRequest:
    path_params: AddBlacklistValuesPathParams = dataclasses.field()
    request: Optional[Any] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class AddBlacklistValuesMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class AddBlacklistValuesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    add_blacklist_values_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    message_general_response: Optional[AddBlacklistValuesMessageGeneralResponse] = dataclasses.field(default=None)
    