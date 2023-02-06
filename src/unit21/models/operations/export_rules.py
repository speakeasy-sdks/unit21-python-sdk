import dataclasses
from ..shared import bulkexportresponse as shared_bulkexportresponse
from dataclasses_json import dataclass_json
from enum import Enum
from typing import Optional
from unit21 import utils

class ExportRulesRequestBodyFiltersStatusesEnum(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    VALIDATION = "VALIDATION"


@dataclass_json
@dataclasses.dataclass
class ExportRulesRequestBodyFilters:
    r"""ExportRulesRequestBodyFilters
    Filter to narrow down rules in export.
    """
    
    agent_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('agent_ids') }})
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('end_date') }})
    rule_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('rule_ids') }})
    start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('start_date') }})
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    statuses: Optional[list[ExportRulesRequestBodyFiltersStatusesEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statuses') }})
    tag_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tag_ids') }})
    

@dataclass_json
@dataclasses.dataclass
class ExportRulesRequestBody:
    filters: Optional[ExportRulesRequestBodyFilters] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filters') }})
    rule_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('rule_ids') }})
    use_csv: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('use_csv') }})
    

@dataclasses.dataclass
class ExportRulesRequest:
    request: Optional[ExportRulesRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class ExportRulesMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class ExportRulesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bulk_export_response: Optional[shared_bulkexportresponse.BulkExportResponse] = dataclasses.field(default=None)
    message_general_response: Optional[ExportRulesMessageGeneralResponse] = dataclasses.field(default=None)
    