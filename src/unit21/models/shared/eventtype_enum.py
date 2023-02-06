import dataclasses
from enum import Enum

class EventTypeEnum(str, Enum):
    TRANSACTION = "transaction"
    ACTION = "action"
