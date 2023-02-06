import dataclasses
from ..shared import investigationstatus_enum as shared_investigationstatus_enum
from ..shared import listcaseresponse as shared_listcaseresponse
from ..shared import sourcearray_enum as shared_sourcearray_enum
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclass_json
@dataclasses.dataclass
class ListCasesRequestBodyOptions:
    r"""ListCasesRequestBodyOptions
    Options for the data included in the returned case. Removing unneeded options can improve response speed.
    """
    
    include_actions: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('include_actions') }})
    include_associations: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('include_associations') }})
    include_checklist: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('include_checklist') }})
    

@dataclass_json
@dataclasses.dataclass
class ListCasesRequestBody:
    r"""ListCasesRequestBody
    To filter your response to a subset of alerts, use these fields.
    """
    
    associated_alerts: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('associated_alerts') }})
    associated_entities: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('associated_entities') }})
    associated_events: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('associated_events') }})
    created_after: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_after') }})
    created_before: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_before') }})
    dispositioned_after: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dispositioned_after') }})
    dispositioned_before: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dispositioned_before') }})
    dispositioned_by: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dispositioned_by') }})
    dispositions: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dispositions') }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('limit') }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('offset') }})
    options: Optional[ListCasesRequestBodyOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('options') }})
    rules: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('rules') }})
    sources: Optional[list[shared_sourcearray_enum.SourceArrayEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sources') }})
    statuses: Optional[list[shared_investigationstatus_enum.InvestigationStatusEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statuses') }})
    

@dataclasses.dataclass
class ListCasesRequest:
    request: Optional[ListCasesRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class ListCasesMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class ListCasesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_case_response: Optional[shared_listcaseresponse.ListCaseResponse] = dataclasses.field(default=None)
    message_general_response: Optional[ListCasesMessageGeneralResponse] = dataclasses.field(default=None)
    