import requests
from . import utils
from typing import Optional
from unit21.models import operations, shared

class InstrumentsAPI:
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

    
    def create_instrument(self, request: operations.CreateInstrumentRequest) -> operations.CreateInstrumentResponse:
        r"""Create an instrument
        Creates a new instrument, sending instrument data in the request body.
        
        Recommended values for `instrument_type` include: account, crypto_address,  digital_wallet, credit_card, debit_card, gift_card, voucher, check, laptop, company_computer, smartphone.
        
        If the `/instruments/create` API is called for an instrument that already exists in our system (i.e.  has an existing `instrument_id`, it is treated it as an  [upsert](https://docs.unit21.ai/reference/should-i-update-or-upsert) and an update on the existing  instrument is performed. The response to the request will then contain the entry `previously_existed: true`. 
        
        Unit21 selectively ignores upserts if the request is identical to a previous request. The response to any  ignored upsert will contain the field `ignored: true`. 
        
        To turn a [placeholder](https://docs.unit21.ai/reference/placeholder-objects) instrument into an instrument in the Unit21 system, use this endpoint.
        
        Updates to an instrument's `instrument_id` are not allowed.
        
        Follow the links for more information:
          - [Relationships](https://docs.unit21.ai/reference/relationships)
          - [Endpoint options](https://docs.unit21.ai/reference/endpoint-options)
          - [Custom data](https://docs.unit21.ai/reference/best-practices-for-custom-data)
          - [Batch uploads](https://docs.unit21.ai/reference/batch-request-examples)
          - [Modifying tags](https://docs.unit21.ai/reference/modifying-tags)
          
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/instruments/create"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateInstrumentResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.create_instrument_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.CreateInstrumentMessageGeneralResponse])
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

    
    def export_instruments(self, request: operations.ExportInstrumentsRequest) -> operations.ExportInstrumentsResponse:
        r"""Bulk export instruments
        Initiates an email and dashboard export of instruments. The export will be as a CSV file.
        
        [Placeholder](https://docs.unit21.ai/reference/placeholder-objects) instruments are not exported.
        
        The agent making the request will need to have the correct permissions for the export to ensure success.
        
        Either the `filters` or the list of `instrument IDs` are required for the export.
        
        **Currently `instrument_ids` should actually be `unit21_ids`.**
        
        Custom data filters are not supported for bulk exports at this time.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/instruments/bulk-export"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ExportInstrumentsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.BulkExportResponse])
                res.bulk_export_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ExportInstrumentsMessageGeneralResponse])
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

    
    def get_instrument(self, request: operations.GetInstrumentRequest) -> operations.GetInstrumentResponse:
        r"""Get an instrument
        Returns all data objects belonging to a single instrument.
        
        [Placeholder](https://docs.unit21.ai/reference/placeholder-objects) instruments are not listed.
        
        This endpoint requires the `instrument_id` which is a unique ID created by your organization to identify the instrument. The `org_name` is your Unit21 appointed organization name such as `google` or `acme`.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/{org_name}/instruments/{instrument_id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetInstrumentResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.instrument_list = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetInstrumentMessageGeneralResponse])
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

    
    def list_instruments(self, request: operations.ListInstrumentsRequest) -> operations.ListInstrumentsResponse:
        r"""List instruments
        Returns paginated list of of top-level information about instruments. 
        
        [Placeholder](https://docs.unit21.ai/reference/placeholder-objects) instruments are not listed.
        
        Because the response is paginated, the request body has a `limit` and `offset` field. At least one must be filled.
        * `limit`  indicates how many objects the request returns (the page maximum is 50)
        * `offset` indicates the offset for pagination. An `offset` value of 1 starts with the environment's first record. The offset is relative to the number of pages (not the total count of objects).
        * `alert_id` is a filter. Only instruments with the associated alert ID will be shown.
        
        The `total_count` field is set to 0. Please call this paginated endpoint, increasing the offset,  until you receive fewer than the maximum number of objects per call.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/instruments/list"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ListInstrumentsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListInstrumentResponse])
                res.list_instrument_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListInstrumentsMessageGeneralResponse])
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

    
    def update_instrument(self, request: operations.UpdateInstrumentRequest) -> operations.UpdateInstrumentResponse:
        r"""Update instrument
        Updates an instrument's information using the `instrument_id` from your platform. 
        
        Updating an instrument has no required fields. You MAY send any  subset of the fields that the `instruments/create` endpoint accepts.
        
        [Placeholder](https://docs.unit21.ai/reference/placeholder-objects) instruments cannot be updated.
        
        This endpoint requires the `instrument_id` which is a unique ID created by your organization to identify the instrument. The `org_name` is your Unit21 appointed organization name such as `google` or `acme`.
        
        Note that you can also update an instrument using an upsert through `/instruments/create`.
        
        Follow the links for more information:
          - [Relationships](https://docs.unit21.ai/reference/relationships)
          - [Endpoint options](https://docs.unit21.ai/reference/endpoint-options)
          - [Custom data](https://docs.unit21.ai/reference/best-practices-for-custom-data)
          - [Batch uploads](https://docs.unit21.ai/reference/batch-request-examples)
          - [Modifying tags](https://docs.unit21.ai/reference/modifying-tags)
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/{org_name}/instruments/{instrument_id}/update", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PUT", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateInstrumentResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.update_instrument_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.UpdateInstrumentMessageGeneralResponse])
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

    