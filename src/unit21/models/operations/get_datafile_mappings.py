import dataclasses
from ..shared import datafilemappingresponse as shared_datafilemappingresponse
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclasses.dataclass
class GetDatafileMappingsPathParams:
    unit21_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'unit21_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetDatafileMappingsRequest:
    path_params: GetDatafileMappingsPathParams = dataclasses.field()
    request: Optional[Any] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class GetDatafileMappingsMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class GetDatafileMappingsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    datafile_mapping_response: Optional[shared_datafilemappingresponse.DatafileMappingResponse] = dataclasses.field(default=None)
    message_general_response: Optional[GetDatafileMappingsMessageGeneralResponse] = dataclasses.field(default=None)
    