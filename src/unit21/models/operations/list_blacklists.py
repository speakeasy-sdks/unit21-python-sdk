import dataclasses
from ..shared import listblacklistresponse as shared_listblacklistresponse
from ..shared import listrequest as shared_listrequest
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclasses.dataclass
class ListBlacklistsRequest:
    request: shared_listrequest.ListRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class ListBlacklistsMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class ListBlacklistsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_blacklist_response: Optional[shared_listblacklistresponse.ListBlacklistResponse] = dataclasses.field(default=None)
    message_general_response: Optional[ListBlacklistsMessageGeneralResponse] = dataclasses.field(default=None)
    