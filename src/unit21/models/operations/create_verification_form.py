import dataclasses
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclass_json
@dataclasses.dataclass
class CreateVerificationFormRequestBody:
    session_length_minutes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('session_length_minutes') }})
    

@dataclasses.dataclass
class CreateVerificationFormRequest:
    request: CreateVerificationFormRequestBody = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class CreateVerificationFormMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class CreateVerificationForm200ApplicationJSON:
    redirect_to: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('redirect_to') }})
    

@dataclasses.dataclass
class CreateVerificationFormResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_verification_form_200_application_json_object: Optional[CreateVerificationForm200ApplicationJSON] = dataclasses.field(default=None)
    message_general_response: Optional[CreateVerificationFormMessageGeneralResponse] = dataclasses.field(default=None)
    