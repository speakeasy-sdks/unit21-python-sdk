import dataclasses
from ..shared import listexportresponse as shared_listexportresponse
from ..shared import listexports as shared_listexports
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclasses.dataclass
class ListExportsRequest:
    request: shared_listexports.ListExports = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class ListExportsMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class ListExportsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_export_response: Optional[shared_listexportresponse.ListExportResponse] = dataclasses.field(default=None)
    message_general_response: Optional[ListExportsMessageGeneralResponse] = dataclasses.field(default=None)
    