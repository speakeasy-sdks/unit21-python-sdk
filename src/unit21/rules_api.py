import requests
from . import utils
from typing import Optional
from unit21.models import operations, shared

class RulesAPI:
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

    
    def export_rules(self, request: operations.ExportRulesRequest) -> operations.ExportRulesResponse:
        r"""Bulk export rules
        Initiates an email and dashboard export of rules. The export will be as a CSV file.
        
        Either the agent `ID` or `email` is required to begin the export.
        
        Either the `filters` or the list of `rule IDs` are required for the export.
        
        **Currently `rule_ids` should actually be `unit21_ids`.**
        
        Custom data filters are not supported for bulk exports at this time.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/rules/bulk-export"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ExportRulesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.BulkExportResponse])
                res.bulk_export_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ExportRulesMessageGeneralResponse])
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

    
    def list_rules(self, request: operations.ListRulesRequest) -> operations.ListRulesResponse:
        r"""List rules
        Returns paginated list of of top-level information about rules.     
        
        Because the response is paginated, the request body has a `limit` and `offset` field. At least one must be filled.
        * `limit`  indicates how many objects the request returns (the page maximum is 50)
        * `offset` indicates the offset for pagination. An `offset` value of 1 starts with the environment's first record. The offset is relative to the number of pages (not the total count of objects).
        
        The `total_count` field contains the total number of rules where the  `response_count` field contains the number of rules included in the response.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/rules/list"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ListRulesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListRuleResponse])
                res.list_rule_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListRulesMessageGeneralResponse])
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

    
    def read_one_rule(self, request: operations.ReadOneRuleRequest) -> operations.ReadOneRuleResponse:
        r"""Get a rule
        Returns all data objects belonging to a single rule.
        
        This endpoint requires the `unit21_id` which is a unique ID created by Unit21 when the rule is first created.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/rules/{unit21_id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ReadOneRuleResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.rule_list = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ReadOneRuleMessageGeneralResponse])
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

    