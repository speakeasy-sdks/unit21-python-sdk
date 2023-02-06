import dataclasses
from enum import Enum

class InvestigationStatusEnum(str, Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
