import dataclasses
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclass_json
@dataclasses.dataclass
class LinkMediaForm:
    form_data: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('form_data') }})
    