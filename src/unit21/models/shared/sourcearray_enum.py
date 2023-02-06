import dataclasses
from enum import Enum

class SourceArrayEnum(str, Enum):
    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"
