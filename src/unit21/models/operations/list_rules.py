import dataclasses
from ..shared import listrequest as shared_listrequest
from ..shared import listruleresponse as shared_listruleresponse
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclasses.dataclass
class ListRulesRequest:
    request: shared_listrequest.ListRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class ListRulesMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class ListRulesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_rule_response: Optional[shared_listruleresponse.ListRuleResponse] = dataclasses.field(default=None)
    message_general_response: Optional[ListRulesMessageGeneralResponse] = dataclasses.field(default=None)
    