import dataclasses
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclasses.dataclass
class GetCaseByUnit21IDPathParams:
    unit21_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'unit21_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetCaseByUnit21IDRequest:
    path_params: GetCaseByUnit21IDPathParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetCaseByUnit21IDMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class GetCaseByUnit21IDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    case_list: Optional[Any] = dataclasses.field(default=None)
    message_general_response: Optional[GetCaseByUnit21IDMessageGeneralResponse] = dataclasses.field(default=None)
    