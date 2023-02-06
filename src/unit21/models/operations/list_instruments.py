import dataclasses
from ..shared import listalertrequest as shared_listalertrequest
from ..shared import listinstrumentresponse as shared_listinstrumentresponse
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclasses.dataclass
class ListInstrumentsRequest:
    request: Optional[shared_listalertrequest.ListAlertRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class ListInstrumentsMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class ListInstrumentsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_instrument_response: Optional[shared_listinstrumentresponse.ListInstrumentResponse] = dataclasses.field(default=None)
    message_general_response: Optional[ListInstrumentsMessageGeneralResponse] = dataclasses.field(default=None)
    