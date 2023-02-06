import dataclasses
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclasses.dataclass
class GetInstrumentPathParams:
    instrument_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'instrument_id', 'style': 'simple', 'explode': False }})
    org_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_name', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetInstrumentRequest:
    path_params: GetInstrumentPathParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetInstrumentMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class GetInstrumentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    instrument_list: Optional[Any] = dataclasses.field(default=None)
    message_general_response: Optional[GetInstrumentMessageGeneralResponse] = dataclasses.field(default=None)
    