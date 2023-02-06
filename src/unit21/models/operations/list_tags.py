import dataclasses
from ..shared import listtagresponse as shared_listtagresponse
from dataclasses_json import dataclass_json
from enum import Enum
from typing import Optional
from unit21 import utils

class ListTagsRequestBodyObjectTypesEnum(str, Enum):
    ALERT = "alert"
    CASE = "case"
    SAR = "sar"
    RULE = "rule"
    AGENT = "agent"
    EVENT = "event"
    ENTITY = "entity"
    INSTRUMENT = "instrument"


@dataclass_json
@dataclasses.dataclass
class ListTagsRequestBody:
    r"""ListTagsRequestBody
    To filter your response to a subset of tag associations, use these fields.
    """
    
    created_after: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_after') }})
    created_before: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_before') }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('limit') }})
    object_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('object_id') }})
    object_types: Optional[list[ListTagsRequestBodyObjectTypesEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('object_types') }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('offset') }})
    tag_filters: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tag_filters') }})
    

@dataclasses.dataclass
class ListTagsRequest:
    request: Optional[ListTagsRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ListTagsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_tag_response: Optional[shared_listtagresponse.ListTagResponse] = dataclasses.field(default=None)
    