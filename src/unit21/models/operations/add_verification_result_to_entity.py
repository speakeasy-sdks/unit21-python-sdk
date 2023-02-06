import dataclasses
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclasses.dataclass
class AddVerificationResultToEntityPathParams:
    unit21_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'unit21_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AddVerificationResultToEntityRequest:
    path_params: AddVerificationResultToEntityPathParams = dataclasses.field()
    request: Optional[Any] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class AddVerificationResultToEntityMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class AddVerificationResultToEntityResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    link_verification_response: Optional[Any] = dataclasses.field(default=None)
    message_general_response: Optional[AddVerificationResultToEntityMessageGeneralResponse] = dataclasses.field(default=None)
    