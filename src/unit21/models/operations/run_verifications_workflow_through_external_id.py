import dataclasses
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclasses.dataclass
class RunVerificationsWorkflowThroughExternalIDPathParams:
    entity_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'entity_id', 'style': 'simple', 'explode': False }})
    org_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_name', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RunVerificationsWorkflowThroughExternalIDRequest:
    path_params: RunVerificationsWorkflowThroughExternalIDPathParams = dataclasses.field()
    request: Any = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class RunVerificationsWorkflowThroughExternalIDMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class RunVerificationsWorkflowThroughExternalID200ApplicationJSON:
    end_action: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('end_action') }})
    full_response: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('full_response') }})
    is_success: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_success') }})
    results: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    

@dataclasses.dataclass
class RunVerificationsWorkflowThroughExternalIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    message_general_response: Optional[RunVerificationsWorkflowThroughExternalIDMessageGeneralResponse] = dataclasses.field(default=None)
    run_verifications_workflow_through_external_id_200_application_json_object: Optional[RunVerificationsWorkflowThroughExternalID200ApplicationJSON] = dataclasses.field(default=None)
    