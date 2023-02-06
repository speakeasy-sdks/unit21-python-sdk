import dataclasses
from ..shared import bulkexportresponse as shared_bulkexportresponse
from dataclasses_json import dataclass_json
from enum import Enum
from typing import Optional
from unit21 import utils

class ExportSarsRequestBodyFiltersReportTypeEnum(str, Enum):
    FINCEN_SAR = "FINCEN_SAR"
    ESTONIAN_FIU = "ESTONIAN_FIU"
    GOAML_STR = "GOAML_STR"
    NCA_SAR = "NCA_SAR"

class ExportSarsRequestBodyFiltersStatusesEnum(str, Enum):
    ARCHIVED = "ARCHIVED"
    PREFILING_VALIDATION_PENDING = "PREFILING_VALIDATION_PENDING"
    PREFILING_VALIDATION_IN_PROCESS = "PREFILING_VALIDATION_IN_PROCESS"
    PREFILING_VALIDATION_FAILED = "PREFILING_VALIDATION_FAILED"
    PREFILING_VALIDATION_SUCCESS = "PREFILING_VALIDATION_SUCCESS"
    QUEUED_FOR_FILING = "QUEUED_FOR_FILING"
    READY_FOR_REVIEW = "READY_FOR_REVIEW"
    SENDING_TO_FINCEN = "SENDING_TO_FINCEN"
    SENT_TO_FINCEN = "SENT_TO_FINCEN"
    FILING_FAILED = "FILING_FAILED"
    FILING_MAX_RETRIES_EXCEEDED = "FILING_MAX_RETRIES_EXCEEDED"
    FILING_SUCCESS = "FILING_SUCCESS"
    FINCEN_VALIDATION_FAILED = "FINCEN_VALIDATION_FAILED"
    FINCEN_REJECTED = "FINCEN_REJECTED"
    FINCEN_STATUS_OTHER = "FINCEN_STATUS_OTHER"
    FINCEN_ACCEPTED = "FINCEN_ACCEPTED"


@dataclass_json
@dataclasses.dataclass
class ExportSarsRequestBodyFilters:
    r"""ExportSarsRequestBodyFilters
    Filter to narrow down sars in export
    """
    
    created_at_end: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at_end') }})
    created_at_start: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at_start') }})
    filed_at_end: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filed_at_end') }})
    filed_at_start: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filed_at_start') }})
    report_type: Optional[ExportSarsRequestBodyFiltersReportTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('report_type') }})
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    statuses: Optional[list[ExportSarsRequestBodyFiltersStatusesEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statuses') }})
    submitted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('submitted') }})
    tag_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tag_ids') }})
    updated_at_end: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('updated_at_end') }})
    updated_at_start: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('updated_at_start') }})
    

@dataclass_json
@dataclasses.dataclass
class ExportSarsRequestBody:
    filters: Optional[ExportSarsRequestBodyFilters] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filters') }})
    sar_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sar_ids') }})
    use_csv: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('use_csv') }})
    

@dataclasses.dataclass
class ExportSarsRequest:
    request: Optional[ExportSarsRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class ExportSarsMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class ExportSarsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bulk_export_response: Optional[shared_bulkexportresponse.BulkExportResponse] = dataclasses.field(default=None)
    message_general_response: Optional[ExportSarsMessageGeneralResponse] = dataclasses.field(default=None)
    