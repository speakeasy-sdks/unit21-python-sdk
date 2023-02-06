import dataclasses
from ..shared import bulkexportresponse as shared_bulkexportresponse
from dataclasses_json import dataclass_json
from enum import Enum
from typing import Optional
from unit21 import utils

class ExportAlertsRequestBodyFiltersAlertTypesEnum(str, Enum):
    CHAINLYSIS = "chainlysis"
    TM = "tm"
    KYC = "kyc"
    MANUAL = "manual"
    CAR = "car"

class ExportAlertsRequestBodyFiltersSourcesEnum(str, Enum):
    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"

class ExportAlertsRequestBodyFiltersStatusesEnum(str, Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"


@dataclass_json
@dataclasses.dataclass
class ExportAlertsRequestBodyFilters:
    r"""ExportAlertsRequestBodyFilters
    Filter to narrow down alerts in export
    """
    
    agent_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('agent_ids') }})
    alert_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('alert_ids') }})
    alert_queue_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('alert_queue_ids') }})
    alert_types: Optional[list[ExportAlertsRequestBodyFiltersAlertTypesEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('alert_types') }})
    alerting_org_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('alerting_org_ids') }})
    disposition: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('disposition') }})
    disposition_end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('disposition_end_date') }})
    disposition_start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('disposition_start_date') }})
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('end_date') }})
    entity_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity_ids') }})
    maximum_amount: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('maximum_amount') }})
    minimum_amount: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('minimum_amount') }})
    phrase: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('phrase') }})
    rule_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('rule_ids') }})
    sources: Optional[list[ExportAlertsRequestBodyFiltersSourcesEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sources') }})
    start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('start_date') }})
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    statuses: Optional[list[ExportAlertsRequestBodyFiltersStatusesEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statuses') }})
    subdisposition_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subdisposition_ids') }})
    subdisposition_option_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('subdisposition_option_ids') }})
    tag_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tag_ids') }})
    team_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('team_ids') }})
    

@dataclass_json
@dataclasses.dataclass
class ExportAlertsRequestBody:
    r"""ExportAlertsRequestBody
    To filter your response.
    """
    
    alert_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('alert_ids') }})
    filters: Optional[ExportAlertsRequestBodyFilters] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filters') }})
    use_csv: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('use_csv') }})
    

@dataclasses.dataclass
class ExportAlertsRequest:
    request: Optional[ExportAlertsRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class ExportAlertsMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class ExportAlertsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bulk_export_response: Optional[shared_bulkexportresponse.BulkExportResponse] = dataclasses.field(default=None)
    message_general_response: Optional[ExportAlertsMessageGeneralResponse] = dataclasses.field(default=None)
    