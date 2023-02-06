import dataclasses
from ..shared import verificationresult as shared_verificationresult
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclasses.dataclass
class GetVerificationResultPathParams:
    result_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'result_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetVerificationResultRequest:
    path_params: GetVerificationResultPathParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetVerificationResultMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class GetVerificationResultResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    message_general_response: Optional[GetVerificationResultMessageGeneralResponse] = dataclasses.field(default=None)
    verification_result: Optional[shared_verificationresult.VerificationResult] = dataclasses.field(default=None)
    