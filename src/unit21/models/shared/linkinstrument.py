import dataclasses
from dataclasses_json import dataclass_json
from typing import Any, Optional
from unit21 import utils


@dataclass_json
@dataclasses.dataclass
class LinkInstrument:
    r"""LinkInstrument
    Associate an instrument directly with an object, like an Entity or Case.
    """
    
    instrument_ids: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('instrument_ids') }})
    