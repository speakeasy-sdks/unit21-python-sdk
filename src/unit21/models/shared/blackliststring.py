import dataclasses
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclass_json
@dataclasses.dataclass
class BlacklistString:
    blacklist_value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('blacklist_value') }})
    