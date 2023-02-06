import dataclasses
from ..shared import continuousmonitoring as shared_continuousmonitoring
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclasses.dataclass
class UpdateContinuousMonitoringPathParams:
    unit21_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'unit21_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateContinuousMonitoringRequest:
    path_params: UpdateContinuousMonitoringPathParams = dataclasses.field()
    request: Optional[shared_continuousmonitoring.ContinuousMonitoring] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class UpdateContinuousMonitoringMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class UpdateContinuousMonitoringResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    message_general_response: Optional[UpdateContinuousMonitoringMessageGeneralResponse] = dataclasses.field(default=None)
    