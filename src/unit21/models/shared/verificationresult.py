import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from typing import Any, Optional
from unit21 import utils

class VerificationResultSourceEnum(str, Enum):
    AU10_TIX = "AU10TIX"
    CHAINALYSIS = "CHAINALYSIS"
    CSI = "CSI"
    DOW_JONES = "DOW_JONES"
    IDOLOGY = "IDOLOGY"
    MITEK = "MITEK"
    SMILE_IDENTITY = "SMILE_IDENTITY"
    TRULIOO = "TRULIOO"
    UNIT21 = "UNIT21"
    EMAILAGE = "EMAILAGE"
    MIDDESK = "MIDDESK"
    SOCURE = "SOCURE"
    NAME_DOB_MATCH = "NAME_DOB_MATCH"
    DOWJONES = "DOWJONES"

class VerificationResultTypeEnum(str, Enum):
    ID_VERIFICATION = "ID_VERIFICATION"
    IDOC_VERIFICATION = "IDOC_VERIFICATION"
    IBUSINESS_VERIFICATION = "IBUSINESS_VERIFICATION"
    ILOGIC = "ILOGIC"
    IWATCHLIST_SCREENING = "IWATCHLIST_SCREENING"
    IADVERSE_MEDIA = "IADVERSE_MEDIA"


@dataclass_json
@dataclasses.dataclass
class VerificationResult:
    r"""VerificationResult
    Verification workflow execution result.
    """
    
    continuous_monitoring: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('continuous_monitoring') }})
    created_at: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at') }})
    entity_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity_id') }})
    full_response: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('full_response') }})
    source: Optional[VerificationResultSourceEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('source') }})
    type: Optional[VerificationResultTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    verification_workflow_execution_id: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('verification_workflow_execution_id') }})
    