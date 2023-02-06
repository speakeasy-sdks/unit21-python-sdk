import dataclasses
from ..shared import verificationresultlist as shared_verificationresultlist
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclasses.dataclass
class GetVerificationResultFromWorkflowExecutionPathParams:
    verification_workflow_execution_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'verification_workflow_execution_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetVerificationResultFromWorkflowExecutionRequest:
    path_params: GetVerificationResultFromWorkflowExecutionPathParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetVerificationResultFromWorkflowExecutionMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class GetVerificationResultFromWorkflowExecutionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    message_general_response: Optional[GetVerificationResultFromWorkflowExecutionMessageGeneralResponse] = dataclasses.field(default=None)
    verification_result_list: Optional[list[shared_verificationresultlist.VerificationResultList]] = dataclasses.field(default=None)
    