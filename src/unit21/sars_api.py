import requests
from . import utils
from typing import Optional
from unit21.models import operations, shared

class SarsAPI:
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

    
    def export_sars(self, request: operations.ExportSarsRequest) -> operations.ExportSarsResponse:
        r"""Bulk export sars
        Initiates an email and dashboard export of sars. The export will be as a CSV file.
        
        Either the agent `ID` or `email` is required to begin the export.
        
        Either the `filters` or the list of `sar IDs` are required for the export.
        
        Custom data filters are not supported for bulk exports at this time.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/sars/bulk-export"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ExportSarsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.BulkExportResponse])
                res.bulk_export_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ExportSarsMessageGeneralResponse])
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

    
    def list_sars(self, request: operations.ListSarsRequest) -> operations.ListSarsResponse:
        r"""List sars
        Returns paginated list of of top-level information about paths/sars@list.yaml    
        
        Because the response is paginated, the request body has a `limit` and `offset` field. At least one must be filled.
        * `limit`  indicates how many objects the request returns (the page maximum is 50)
        * `offset` indicates the offset for pagination. An `offset` value of 1 starts with the environment's first record. The offset is relative to the number of pages (not the total count of objects).
        
        To narrow down your sars search, we provide filter parameters to this endpoint. Note that all list inputs function as an \"or\" filter, as in any one of the values must match the selected sar(s):
        
        
          | Field                   | Type        | Description                                                                                                       |
          | ----------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------- |
          | `created_after`         | Numeric     | SARs created on or after this unix timestamp                                                                      |
          | `created_before`        | Numeric     | SARs created before this unix timestamp                                                                           |
          | `tag_filters`           | String[]    | List of string tags (`key:value`) or keys to associate this SARs with (e.g. `sars_type:high_velocity` or `sars_type`). If only the key is provided, we will match against all tags with that key        |
          | `limit`                 | Numeric     | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10          |
          | `offset`                | Numeric     | The offset for pagination. Default is 1                                                                           |
          | `options`               | Object      | Options for the data included in the returned SARs. Removing unneeded options can improve response speed          |
        
        
        The `total_count` field contains the total number of sars where the  `response_count` field contains the number of sars included in the response.
        
        Follow the links for more information:
          - [Endpoint options](https://docs.unit21.ai/reference/endpoint-options)
          
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/sars/list"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ListSarsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListSarResponse])
                res.list_sar_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListSarsMessageGeneralResponse])
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

    
    def read_one_sar(self, request: operations.ReadOneSarRequest) -> operations.ReadOneSarResponse:
        r"""Get a sars
        Returns all data objects belonging to a single SAR.
        
        This endpoint requires the `unit21_id` which is a unique ID created by Unit21 when the sar is first created.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/sars/{unit21_id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ReadOneSarResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.sar_list = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ReadOneSarMessageGeneralResponse])
                res.message_general_response = out

        return res

    