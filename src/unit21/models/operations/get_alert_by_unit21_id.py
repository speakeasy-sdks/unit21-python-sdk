import dataclasses
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclasses.dataclass
class GetAlertByUnit21IDPathParams:
    unit21_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'unit21_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetAlertByUnit21IDRequest:
    path_params: GetAlertByUnit21IDPathParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetAlertByUnit21IDMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class GetAlertByUnit21IDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    alert_list: Optional[Any] = dataclasses.field(default=None)
    message_general_response: Optional[GetAlertByUnit21IDMessageGeneralResponse] = dataclasses.field(default=None)
    