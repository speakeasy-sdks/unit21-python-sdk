import dataclasses
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclass_json
@dataclasses.dataclass
class SuppressProviderEntity:
    provider_entity_ids: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('provider_entity_ids') }})
    suppress: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('suppress') }})
    synchronous_response: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('synchronous_response') }})
    