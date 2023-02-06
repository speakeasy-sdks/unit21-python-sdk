import dataclasses
from ..shared import listsarresponse as shared_listsarresponse
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclass_json
@dataclasses.dataclass
class ListSarsRequestBodyOptions:
    r"""ListSarsRequestBodyOptions
    Options for the data included in the returned case. Removing unneeded options can improve response speed.
    """
    
    include_associations: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('include_associations') }})
    

@dataclass_json
@dataclasses.dataclass
class ListSarsRequestBody:
    r"""ListSarsRequestBody
    To filter your response to a subset of sars, use these fields.
    """
    
    created_after: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_after') }})
    created_before: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_before') }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('limit') }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('offset') }})
    options: Optional[ListSarsRequestBodyOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('options') }})
    tag_filters: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tag_filters') }})
    

@dataclasses.dataclass
class ListSarsRequest:
    request: Optional[ListSarsRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class ListSarsMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class ListSarsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_sar_response: Optional[shared_listsarresponse.ListSarResponse] = dataclasses.field(default=None)
    message_general_response: Optional[ListSarsMessageGeneralResponse] = dataclasses.field(default=None)
    