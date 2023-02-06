import dataclasses
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclasses.dataclass
class UpdateWebhookPathParams:
    unit21_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'unit21_id', 'style': 'simple', 'explode': False }})
    

@dataclass_json
@dataclasses.dataclass
class UpdateWebhookRequestBody:
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('url') }})
    

@dataclasses.dataclass
class UpdateWebhookRequest:
    path_params: UpdateWebhookPathParams = dataclasses.field()
    request: Optional[UpdateWebhookRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateWebhookResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    