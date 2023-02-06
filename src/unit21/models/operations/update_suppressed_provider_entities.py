import dataclasses
from ..shared import suppressproviderentity as shared_suppressproviderentity
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclasses.dataclass
class UpdateSuppressedProviderEntitiesPathParams:
    unit21_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'unit21_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateSuppressedProviderEntitiesRequest:
    path_params: UpdateSuppressedProviderEntitiesPathParams = dataclasses.field()
    request: Optional[shared_suppressproviderentity.SuppressProviderEntity] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class UpdateSuppressedProviderEntitiesMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class UpdateSuppressedProviderEntitiesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    message_general_response: Optional[UpdateSuppressedProviderEntitiesMessageGeneralResponse] = dataclasses.field(default=None)
    