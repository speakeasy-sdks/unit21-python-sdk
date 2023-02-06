import dataclasses
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclass_json
@dataclasses.dataclass
class ListEventResponse:
    events: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('events') }})
    response_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('response_count') }})
    total_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('total_count') }})
    