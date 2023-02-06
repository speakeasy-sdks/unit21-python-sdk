import dataclasses
from ..shared import verificationlist as shared_verificationlist
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclasses.dataclass
class GetEntityVerificationWorkflowExecutionsPathParams:
    unit21_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'unit21_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetEntityVerificationWorkflowExecutionsRequest:
    path_params: GetEntityVerificationWorkflowExecutionsPathParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetEntityVerificationWorkflowExecutionsMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class GetEntityVerificationWorkflowExecutionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    message_general_response: Optional[GetEntityVerificationWorkflowExecutionsMessageGeneralResponse] = dataclasses.field(default=None)
    verification_list: Optional[list[shared_verificationlist.VerificationList]] = dataclasses.field(default=None)
    