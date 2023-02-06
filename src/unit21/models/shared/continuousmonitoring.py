import dataclasses
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclass_json
@dataclasses.dataclass
class ContinuousMonitoring:
    continuous_monitoring: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('continuous_monitoring') }})
    synchronous_response: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('synchronous_response') }})
    