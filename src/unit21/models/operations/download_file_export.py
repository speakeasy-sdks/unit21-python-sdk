import dataclasses
from ..shared import listexporturlresponse as shared_listexporturlresponse
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclasses.dataclass
class DownloadFileExportPathParams:
    file_export_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'file_export_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DownloadFileExportRequest:
    path_params: DownloadFileExportPathParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class DownloadFileExportMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class DownloadFileExportResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_export_url_response: Optional[shared_listexporturlresponse.ListExportURLResponse] = dataclasses.field(default=None)
    message_general_response: Optional[DownloadFileExportMessageGeneralResponse] = dataclasses.field(default=None)
    