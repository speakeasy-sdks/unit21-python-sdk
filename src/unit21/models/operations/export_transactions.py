import dataclasses
from ..shared import bulkexportresponse as shared_bulkexportresponse
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclass_json
@dataclasses.dataclass
class ExportTransactionsRequestBodyFilters:
    r"""ExportTransactionsRequestBodyFilters
    Filter to narrow down events in export
    """
    
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('end_date') }})
    entity_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity_ids') }})
    maximum_amount: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('maximum_amount') }})
    minimum_amount: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('minimum_amount') }})
    start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('start_date') }})
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    statuses: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statuses') }})
    tag_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tag_ids') }})
    

@dataclass_json
@dataclasses.dataclass
class ExportTransactionsRequestBody:
    event_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('event_ids') }})
    filters: Optional[ExportTransactionsRequestBodyFilters] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filters') }})
    use_csv: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('use_csv') }})
    

@dataclasses.dataclass
class ExportTransactionsRequest:
    request: Optional[ExportTransactionsRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class ExportTransactionsMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class ExportTransactionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bulk_export_response: Optional[shared_bulkexportresponse.BulkExportResponse] = dataclasses.field(default=None)
    message_general_response: Optional[ExportTransactionsMessageGeneralResponse] = dataclasses.field(default=None)
    