import dataclasses
from ..shared import listentityrequest as shared_listentityrequest
from ..shared import listentityresponse as shared_listentityresponse
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclasses.dataclass
class ListEntitiesRequest:
    request: Optional[shared_listentityrequest.ListEntityRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class ListEntitiesMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class ListEntitiesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_entity_response: Optional[shared_listentityresponse.ListEntityResponse] = dataclasses.field(default=None)
    message_general_response: Optional[ListEntitiesMessageGeneralResponse] = dataclasses.field(default=None)
    