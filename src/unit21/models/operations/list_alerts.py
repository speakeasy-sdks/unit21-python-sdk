import dataclasses
from ..shared import investigationstatus_enum as shared_investigationstatus_enum
from ..shared import listalertresponse as shared_listalertresponse
from ..shared import sourcearray_enum as shared_sourcearray_enum
from dataclasses_json import dataclass_json
from enum import Enum
from typing import Optional
from unit21 import utils


@dataclass_json
@dataclasses.dataclass
class ListAlertsRequestBodyOptions:
    r"""ListAlertsRequestBodyOptions
    Options for the data included in the returned alerts. Removing unneeded options can improve response speed.
    """
    
    include_actions: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('include_actions') }})
    include_associations: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('include_associations') }})
    include_checklist: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('include_checklist') }})
    
class ListAlertsRequestBodyTypesEnum(str, Enum):
    TM = "tm"
    KYC = "kyc"
    CHAINALYSIS = "chainalysis"
    MANUAL = "manual"
    CAR = "car"


@dataclass_json
@dataclasses.dataclass
class ListAlertsRequestBody:
    r"""ListAlertsRequestBody
    To filter your response to a subset of alerts, use these fields.
    """
    
    limit: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('limit') }})
    offset: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('offset') }})
    associated_entities: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('associated_entities') }})
    associated_events: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('associated_events') }})
    associated_instruments: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('associated_instruments') }})
    case_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('case_id') }})
    created_after: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_after') }})
    created_before: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_before') }})
    dispositioned_after: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dispositioned_after') }})
    dispositioned_before: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dispositioned_before') }})
    dispositioned_by: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dispositioned_by') }})
    dispositions: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dispositions') }})
    options: Optional[ListAlertsRequestBodyOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('options') }})
    rules: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('rules') }})
    sources: Optional[list[shared_sourcearray_enum.SourceArrayEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sources') }})
    statuses: Optional[list[shared_investigationstatus_enum.InvestigationStatusEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statuses') }})
    tag_filters: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tag_filters') }})
    types: Optional[list[ListAlertsRequestBodyTypesEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('types') }})
    

@dataclasses.dataclass
class ListAlertsRequest:
    request: Optional[ListAlertsRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class ListAlertsMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class ListAlertsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_alert_response: Optional[shared_listalertresponse.ListAlertResponse] = dataclasses.field(default=None)
    message_general_response: Optional[ListAlertsMessageGeneralResponse] = dataclasses.field(default=None)
    