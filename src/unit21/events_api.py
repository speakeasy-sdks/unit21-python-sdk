import requests
from . import utils
from typing import Optional
from unit21.models import operations, shared

class EventsAPI:
    _client: requests.Session
    _security_client: requests.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests.Session, security_client: requests.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version

    
    def create_event(self, request: operations.CreateEventRequest) -> operations.CreateEventResponse:
        r"""Create an event
        Creates a new event, sending event data in the request body. 
        
        Two objects are required: `general_data` and either `transaction_data` or `action_data`. `general_data` requires the fields: `event_id`, `event_type`, and `event_time`. `transaction_data` requires only the field `amount`.
        
        Unlike entities, events on our system are cannot be explicitly updated. However, they can be  overwritten in a naive upsert-overwrite fashion. 
        
        If we receive a request to create an event for an `event_id` that already exists in our system,  we will simply overwrite that previous entry with the newly provided data if this transaction  is not already associated with other articles in our system. 
        
        For instance, if a transaction is flagged in an alert and we receive a request to overwrite  the details of this transaction, we will respond with a **409 error code** indicating that this  event cannot be overwritten.
        
        Updates to an event's `general_data.event_id` are not allowed.
        
        Follow the links for more information:
          - [Endpoint options](https://docs.unit21.ai/reference/endpoint-options)
          - [Verification options](https://docs.unit21.ai/reference/identity-verification-options)
          - [Custom data](https://docs.unit21.ai/reference/best-practices-for-custom-data)
          - [Batch uploads](https://docs.unit21.ai/reference/batch-request-examples)
          - [Modifying tags](https://docs.unit21.ai/reference/modifying-tags)
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/events/create"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateEventResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.create_event_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.CreateEventMessageGeneralResponse])
                res.message_general_response = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 403:
            pass
        elif r.status_code == 404:
            pass
        elif r.status_code == 409:
            pass
        elif r.status_code == 423:
            pass
        elif r.status_code == 429:
            pass
        elif r.status_code == 500:
            pass
        elif r.status_code == 503:
            pass

        return res

    
    def export_events(self, request: operations.ExportEventsRequest) -> operations.ExportEventsResponse:
        r"""Bulk export events
        Initiates an email and dashboard export of events. The export will be as a CSV file.
        
        Either the agent `ID` or `email` is required to begin the export.
        
        Either the `filters` or the list of `event IDs` are required for the export.
        
        **Currently `event_ids` should actually be `unit21_ids`.**
        
        Custom data filters are not supported for bulk exports at this time.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/events/bulk-export"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ExportEventsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.BulkExportResponse])
                res.bulk_export_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ExportEventsMessageGeneralResponse])
                res.message_general_response = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 403:
            pass
        elif r.status_code == 404:
            pass
        elif r.status_code == 409:
            pass
        elif r.status_code == 423:
            pass
        elif r.status_code == 429:
            pass
        elif r.status_code == 500:
            pass
        elif r.status_code == 503:
            pass

        return res

    
    def export_transactions(self, request: operations.ExportTransactionsRequest) -> operations.ExportTransactionsResponse:
        r"""Bulk export transactions
        Initiates an email and dashboard export of events. The export will be as a CSV file.
        
        Either the agent `ID` or `email` is required to begin the export.
        
        Either the `filters` or the list of `event IDs` are required for the export.
        
        **Currently `event_ids` should actually be `unit21_ids`.**
        
        Custom data filters are not supported for bulk exports at this time.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/txn-events/bulk-export"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ExportTransactionsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.BulkExportResponse])
                res.bulk_export_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ExportTransactionsMessageGeneralResponse])
                res.message_general_response = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 403:
            pass
        elif r.status_code == 404:
            pass
        elif r.status_code == 409:
            pass
        elif r.status_code == 423:
            pass
        elif r.status_code == 429:
            pass
        elif r.status_code == 500:
            pass
        elif r.status_code == 503:
            pass

        return res

    
    def get_event(self, request: operations.GetEventRequest) -> operations.GetEventResponse:
        r"""Get an event
        Returns all data objects belonging to a single event.
        
        This endpoint requires the `events_id` which is a unique ID created by your organization to identify the event. The `org_name` is your Unit21 appointed organization name such as `google` or `acme`.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/{org_name}/events/{event_id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetEventResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.event_list = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetEventMessageGeneralResponse])
                res.message_general_response = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 403:
            pass
        elif r.status_code == 404:
            pass
        elif r.status_code == 409:
            pass
        elif r.status_code == 429:
            pass
        elif r.status_code == 500:
            pass
        elif r.status_code == 503:
            pass

        return res

    
    def list_events(self, request: operations.ListEventsRequest) -> operations.ListEventsResponse:
        r"""List events
        Returns an array of top-level information about events in your environment.
        
        Because the response is paginated, the request body has a `limit` and `offset` field. At least one must be filled.
        * `limit`  indicates how many objects the request returns (the page maximum is 50)
        * `offset` indicates the offset for pagination. An `offset` value of 1 starts with the environment's first record.
        * `case_id`  is a filter. Only events with the associated case ID will be shown.
        * `alert_id` is a filter. Only events with the associated alert ID will be shown.
        * `start_date`  is a filter. Only events that started on or after this date will be shown.
        * `end_date` is a filter. Only events that ended on or before this date will be shown.
        
        The `total_count` field is set to 0. Please call this paginated endpoint, increasing the offset,  until you receive fewer than the maximum number of objects per call.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/events/list"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ListEventsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListEventResponse])
                res.list_event_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListEventsMessageGeneralResponse])
                res.message_general_response = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 403:
            pass
        elif r.status_code == 404:
            pass
        elif r.status_code == 409:
            pass
        elif r.status_code == 423:
            pass
        elif r.status_code == 429:
            pass
        elif r.status_code == 500:
            pass
        elif r.status_code == 503:
            pass

        return res

    
    def update_event(self, request: operations.UpdateEventRequest) -> operations.UpdateEventResponse:
        r"""Update event
        Update an event using the `event_id` from your platform. 
        
        Updating an event has no required fields. You MAY send any  subset of the fields that the events/create endpoint accepts.
        
        This endpoint requires the `event_id` which is a unique ID created by your organization to identify the event. The `org_name` is your Unit21 appointed organization name such as `google` or `acme`.
        
        Note that you can also update an event using an upsert through `/events/create`.
        
        Follow the links for more information:
          - [Endpoint options](https://docs.unit21.ai/reference/endpoint-options)
          - [Custom data](https://docs.unit21.ai/reference/best-practices-for-custom-data)
          - [Batch uploads](https://docs.unit21.ai/reference/batch-request-examples)
          - [Modifying tags](https://docs.unit21.ai/reference/modifying-tags)
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/{org_name}/events/{event_id}/update", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PUT", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateEventResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.update_event_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.UpdateEventMessageGeneralResponse])
                res.message_general_response = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 403:
            pass
        elif r.status_code == 404:
            pass
        elif r.status_code == 409:
            pass
        elif r.status_code == 423:
            pass
        elif r.status_code == 429:
            pass
        elif r.status_code == 500:
            pass
        elif r.status_code == 503:
            pass

        return res

    