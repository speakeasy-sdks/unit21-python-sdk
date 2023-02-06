import dataclasses
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclasses.dataclass
class UpdateInstrumentPathParams:
    instrument_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'instrument_id', 'style': 'simple', 'explode': False }})
    org_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_name', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateInstrumentRequest:
    path_params: UpdateInstrumentPathParams = dataclasses.field()
    request: Optional[Any] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class UpdateInstrumentMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class UpdateInstrumentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    message_general_response: Optional[UpdateInstrumentMessageGeneralResponse] = dataclasses.field(default=None)
    update_instrument_response: Optional[Any] = dataclasses.field(default=None)
    