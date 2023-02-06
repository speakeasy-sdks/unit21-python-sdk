import dataclasses
from ..shared import eventtype_enum as shared_eventtype_enum
from ..shared import locationdataproperties as shared_locationdataproperties
from dataclasses_json import dataclass_json
from enum import Enum
from typing import Any, Optional
from unit21 import utils


@dataclass_json
@dataclasses.dataclass
class CreateEventEventOptionsActionData:
    r"""CreateEventEventOptionsActionData
    Information about any notable actions that a user takes on your system. Examples of actions that may be worth tracking are:
      * Password changes from new IP addresses
      * Logins from disparate locations
      * Linking or unlinking instruments at an unusual frequency
      * Finding users frequently using referral codes, potentially signally fake referral schemes.
    
    """
    
    entity_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity_id') }})
    entity_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity_type') }})
    action_details: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('action_details') }})
    action_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('action_type') }})
    instrument_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('instrument_id') }})
    

@dataclass_json
@dataclasses.dataclass
class CreateEventEventOptionsDigitalData:
    r"""CreateEventEventOptionsDigitalData
    Associated digital properties - IP, device, browser, client info etc.
    """
    
    client_fingerprint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('client_fingerprint') }})
    ip_address: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ip_address') }})
    

@dataclass_json
@dataclasses.dataclass
class CreateEventEventOptionsGeneralData:
    r"""CreateEventEventOptionsGeneralData
    General data is required for any request made to the v1/events/create endpoint. This defines any pieces of information that allows you to link up any event on Unit21's system to transactions or user activities on your platform.
    
    """
    
    event_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('event_id') }})
    event_time: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('event_time') }})
    event_type: shared_eventtype_enum.EventTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('event_type') }})
    event_subtype: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('event_subtype') }})
    parents: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('parents') }})
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tags') }})
    
class CreateEventEventOptionsOptionsLinkedEntityEnum(str, Enum):
    SENDER = "sender"
    RECEIVER = "receiver"
    BOTH = "both"


@dataclass_json
@dataclasses.dataclass
class CreateEventEventOptionsOptions:
    link_digital_data_to_entity: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('link_digital_data_to_entity') }})
    linked_entity: Optional[CreateEventEventOptionsOptionsLinkedEntityEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('linked_entity') }})
    merge_custom_data: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('merge_custom_data') }})
    monitor: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('monitor') }})
    resolve_geoip: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('resolve_geoip') }})
    upsert_on_conflict: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('upsert_on_conflict') }})
    

@dataclass_json
@dataclasses.dataclass
class CreateEventEventOptionsTransactionData:
    r"""CreateEventEventOptionsTransactionData
    In addition to the required `amount` field, must include at least one of:
    * `sender_entity_id`
    * `sender_instrument_id`
    * `receiver_entity_id`
    * `receiver_instrument_id`
    
    """
    
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount') }})
    exchange_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('exchange_rate') }})
    external_fee: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('external_fee') }})
    internal_fee: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('internal_fee') }})
    received_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('received_amount') }})
    received_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('received_currency') }})
    receiver_entity_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('receiver_entity_id') }})
    receiver_entity_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('receiver_entity_type') }})
    receiver_instrument_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('receiver_instrument_id') }})
    sender_entity_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sender_entity_id') }})
    sender_entity_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sender_entity_type') }})
    sender_instrument_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sender_instrument_id') }})
    sent_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sent_amount') }})
    sent_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sent_currency') }})
    transaction_hash: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transaction_hash') }})
    usd_conversion_notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('usd_conversion_notes') }})
    

@dataclass_json
@dataclasses.dataclass
class CreateEventEventOptions:
    action_data: Optional[CreateEventEventOptionsActionData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('action_data') }})
    custom_data: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('custom_data') }})
    digital_data: Optional[CreateEventEventOptionsDigitalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('digital_data') }})
    general_data: Optional[CreateEventEventOptionsGeneralData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('general_data') }})
    location_data: Optional[shared_locationdataproperties.LocationDataProperties] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('location_data') }})
    options: Optional[CreateEventEventOptionsOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('options') }})
    transaction_data: Optional[CreateEventEventOptionsTransactionData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transaction_data') }})
    

@dataclasses.dataclass
class CreateEventRequest:
    request: Optional[CreateEventEventOptions] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class CreateEventMessageGeneralResponse:
    error_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class CreateEventResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_event_response: Optional[Any] = dataclasses.field(default=None)
    message_general_response: Optional[CreateEventMessageGeneralResponse] = dataclasses.field(default=None)
    