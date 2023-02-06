import dataclasses
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclasses.dataclass
class GetVerificationWorkflowExecutionPathParams:
    verification_workflow_execution_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'verification_workflow_execution_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetVerificationWorkflowExecutionRequest:
    path_params: GetVerificationWorkflowExecutionPathParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetVerificationWorkflowExecutionMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class GetVerificationWorkflowExecutionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    message_general_response: Optional[GetVerificationWorkflowExecutionMessageGeneralResponse] = dataclasses.field(default=None)
    verification: Optional[Any] = dataclasses.field(default=None)
    