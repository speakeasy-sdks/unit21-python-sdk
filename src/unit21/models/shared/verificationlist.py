import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from typing import Optional
from unit21 import utils

class VerificationListEndActionEnum(str, Enum):
    DOLLAR_REJECT = "$REJECT"
    DOLLAR_OTHER = "$OTHER"
    DOLLAR_MANUAL_VERIFICATION = "$MANUAL_VERIFICATION"
    DOLLAR_RESUBMIT = "$RESUBMIT"
    DOLLAR_ACCEPT = "$ACCEPT"


@dataclass_json
@dataclasses.dataclass
class VerificationList:
    created_at: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at') }})
    end_action: Optional[VerificationListEndActionEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('end_action') }})
    verification_workflow_execution_id: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('verification_workflow_execution_id') }})
    