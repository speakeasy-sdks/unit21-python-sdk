import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from typing import Any, Optional
from unit21 import utils

class VerificationResultListContentGenerateAlertActionsEnum(str, Enum):
    DOLLAR_REJECT = "$REJECT"
    DOLLAR_OTHER = "$OTHER"
    DOLLAR_MANUAL_VERIFICATION = "$MANUAL_VERIFICATION"
    DOLLAR_RESUBMIT = "$RESUBMIT"
    DOLLAR_ACCEPT = "$ACCEPT"

class VerificationResultListContentStartActionEnum(str, Enum):
    TRULIOO_ID_VERIFICATION = "TRULIOO:ID_VERIFICATION"
    CSI_WATCHLIST_SCREENING = "CSI:WATCHLIST_SCREENING"
    IDOLOGY_ID_VERIFICATION = "IDOLOGY:ID_VERIFICATION"
    IDOLOGY_DOC_VERIFICATION = "IDOLOGY:DOC_VERIFICATION"
    JUMIO_DOC_VERIFICATION = "JUMIO:DOC_VERIFICATION"
    IDOLOGY_WATCHLIST_SCREENING = "IDOLOGY:WATCHLIST_SCREENING"
    EMAILAGE_ID_VERIFICATION = "EMAILAGE:ID_VERIFICATION"
    UNIT21_BUSINESS_VERIFICATION = "UNIT21:BUSINESS_VERIFICATION"
    UNIT21_ID_VERIFICATION = "UNIT21:ID_VERIFICATION"
    AU10_TIX_DOC_VERIFICATION = "AU10TIX:DOC_VERIFICATION"
    MIDDESK_BUSINESS_VERIFICATION = "MIDDESK:BUSINESS_VERIFICATION"
    SOCURE_ID_VERIFICATION = "SOCURE:ID_VERIFICATION"
    SOCURE_DOC_VERIFICATION = "SOCURE:DOC_VERIFICATION"
    SOCURE_WATCHLIST_EVENT = "SOCURE:WATCHLIST_EVENT"
    NAME_DOB_MATCH_ID_VERIFICATION = "NAME_DOB_MATCH:ID_VERIFICATION"
    EXISTING_VERIFICATION_ID_VERIFICATION = "EXISTING_VERIFICATION:ID_VERIFICATION"
    UNIT21_LOGIC = "UNIT21:LOGIC"
    DOW_JONES_ADVERSE_MEDIA = "DOW_JONES:ADVERSE_MEDIA"


@dataclass_json
@dataclasses.dataclass
class VerificationResultListContent:
    actions: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('actions') }})
    generate_alert_actions: Optional[list[VerificationResultListContentGenerateAlertActionsEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('generate_alert_actions') }})
    start_action: Optional[VerificationResultListContentStartActionEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('start_action') }})
    
class VerificationResultListSourceEnum(str, Enum):
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

class VerificationResultListTypeEnum(str, Enum):
    ID_VERIFICATION = "ID_VERIFICATION"
    IDOC_VERIFICATION = "IDOC_VERIFICATION"
    IBUSINESS_VERIFICATION = "IBUSINESS_VERIFICATION"
    ILOGIC = "ILOGIC"
    IWATCHLIST_SCREENING = "IWATCHLIST_SCREENING"
    IADVERSE_MEDIA = "IADVERSE_MEDIA"


@dataclass_json
@dataclasses.dataclass
class VerificationResultList:
    alert_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('alert_id') }})
    content: Optional[VerificationResultListContent] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('content') }})
    continuous_monitoring: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('continuous_monitoring') }})
    created_at: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at') }})
    id: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    source: Optional[VerificationResultListSourceEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('source') }})
    type: Optional[VerificationResultListTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    verification_workflow_execution_id: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('verification_workflow_execution_id') }})
    