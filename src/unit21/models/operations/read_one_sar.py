import dataclasses
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclasses.dataclass
class ReadOneSarPathParams:
    unit21_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'unit21_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ReadOneSarRequest:
    path_params: ReadOneSarPathParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class ReadOneSarMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class ReadOneSarResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    message_general_response: Optional[ReadOneSarMessageGeneralResponse] = dataclasses.field(default=None)
    sar_list: Optional[Any] = dataclasses.field(default=None)
    