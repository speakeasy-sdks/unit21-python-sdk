import dataclasses
from ..shared import listdaterequest as shared_listdaterequest
from ..shared import listeventresponse as shared_listeventresponse
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclasses.dataclass
class ListEventsRequest:
    request: Optional[shared_listdaterequest.ListDateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class ListEventsMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class ListEventsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_event_response: Optional[shared_listeventresponse.ListEventResponse] = dataclasses.field(default=None)
    message_general_response: Optional[ListEventsMessageGeneralResponse] = dataclasses.field(default=None)
    