import dataclasses
from ..shared import bulkexportresponse as shared_bulkexportresponse
from dataclasses_json import dataclass_json
from enum import Enum
from typing import Optional
from unit21 import utils

class ExportCasesRequestBodyFiltersStatusesEnum(str, Enum):
    OPEN = "open"
    CLOSED = "closed"


@dataclass_json
@dataclasses.dataclass
class ExportCasesRequestBodyFilters:
    r"""ExportCasesRequestBodyFilters
    Filter to narrow down cases in export
    """
    
    agent_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('agent_ids') }})
    case_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('case_ids') }})
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('end_date') }})
    maximum_amount: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('maximum_amount') }})
    minimum_amount: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('minimum_amount') }})
    rule_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('rule_ids') }})
    start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('start_date') }})
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    statuses: Optional[list[ExportCasesRequestBodyFiltersStatusesEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statuses') }})
    tag_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tag_ids') }})
    team_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('team_ids') }})
    

@dataclass_json
@dataclasses.dataclass
class ExportCasesRequestBody:
    r"""ExportCasesRequestBody
    To filter your response.
    """
    
    case_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('case_ids') }})
    filters: Optional[ExportCasesRequestBodyFilters] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filters') }})
    use_csv: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('use_csv') }})
    

@dataclasses.dataclass
class ExportCasesRequest:
    request: Optional[ExportCasesRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class ExportCasesMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class ExportCasesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bulk_export_response: Optional[shared_bulkexportresponse.BulkExportResponse] = dataclasses.field(default=None)
    message_general_response: Optional[ExportCasesMessageGeneralResponse] = dataclasses.field(default=None)
    