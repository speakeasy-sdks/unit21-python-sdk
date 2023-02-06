import dataclasses
from dataclasses_json import dataclass_json
from typing import Optional
from unit21 import utils


@dataclass_json
@dataclasses.dataclass
class DatafileMappingResponseEntityList:
    entity_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity_id') }})
    unit21_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('unit21_id') }})
    

@dataclass_json
@dataclasses.dataclass
class DatafileMappingResponseEventList:
    event_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('event_id') }})
    unit21_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('unit21_id') }})
    

@dataclass_json
@dataclasses.dataclass
class DatafileMappingResponseInstrumentList:
    instrument_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('instrument_id') }})
    unit21_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('unit21_id') }})
    

@dataclass_json
@dataclasses.dataclass
class DatafileMappingResponse:
    entity_list: Optional[list[DatafileMappingResponseEntityList]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity_list') }})
    event_list: Optional[list[DatafileMappingResponseEventList]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('event_list') }})
    instrument_list: Optional[list[DatafileMappingResponseInstrumentList]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('instrument_list') }})
    