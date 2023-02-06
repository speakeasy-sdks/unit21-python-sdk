import dataclasses
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclasses.dataclass
class CreateDatafilesRequest:
    request: Any = dataclasses.field(metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclass_json
@dataclasses.dataclass
class CreateDatafilesMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class CreateDatafilesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_datafile_response: Optional[Any] = dataclasses.field(default=None)
    message_general_response: Optional[CreateDatafilesMessageGeneralResponse] = dataclasses.field(default=None)
    