import requests
from . import utils
from typing import Optional
from unit21.models import operations, shared

class MatchlistsAPI:
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

    
    def add_blacklist_values(self, request: operations.AddBlacklistValuesRequest) -> operations.AddBlacklistValuesResponse:
        r"""Add items to a matchlist
        Add items to a matchlist, according to the matchist's `type`.
        
        Each request must specify at least **1** object to matchlist. You may add up to **100**  values to an existing matchlist at once.
        
        The `/blacklists/<blacklist-id>/add-values` API will ignore entries provided that already exist  in the matchlist. No error will be thrown when this occurs.
        
        The response will consist of the following fields:
        
          | Type       | Description                                                              | Example                           |
          |------------|--------------------------------------------------------------------------|-----------------------------------|
          | `STRING`	 | Plain strings to match against any text-type field.                      |   \"blacklist_value\": \"abcde\"      |
          | `IP_INET`	 | IPv4 or IPv6 IP addresses to matchlist.                                  | 	\"ip_address\": \"255.255.255.255\" |
          | `IP_CIDR`	 | Classless Inter-Domain Routing (CIDR) [notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation) IP address ranges to blacklist.  | 	\"cidr\": \"255.255.255.255/32\" |
          | `USER`	   | 	Series of fields that a Unit21 user entity will be matched against.     | 	user_data object                |
          | `BUSINESS` | Series of fields that a Unit21 business entity will be matched against.  | 	business_data object            |
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/blacklists/{unit21_id}/add-values", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.AddBlacklistValuesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.add_blacklist_values_200_application_json_any = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.AddBlacklistValuesMessageGeneralResponse])
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

    
    def create_blacklist(self, request: operations.CreateBlacklistRequest) -> operations.CreateBlacklistResponse:
        r"""Create a matchlist
        Create a new matchlist sending matchlist data in the request body. 
        
        Unit21 currently supports 5 types of matchlists:
        
          * `STRING`: Plain strings to match against any text-type field.
          * `IP_INET`: IPv4 or IPv6 IP addresses to matchlist.
          * `IP_CIDR`: [Classless Inter-Domain Routing (CIDR) notation IP address ranges](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation) to blacklist, 
          * `USER`: Series of fields that a Unit21 user entity will be matched against.
          * `BUSINESS`: Series of fields that a Unit21 business entity will be matched against.
        
        
        If the `/blacklists/create` API is called multiple times, it will create a new matchlist each time.  This endpoint does not support updates/upserts.
        
        This endpoint does not support batch uploads.
        
        The response will consist of the following fields:
        
          | Field           | Type     | Description                                           |
          |-----------------|----------|-------------------------------------------------------|
          | `blacklist_id`  | String   | 	Unique identifier of the entity on your platform     |
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/blacklists/create"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateBlacklistResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.create_blacklist_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.CreateBlacklistMessageGeneralResponse])
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

    
    def list_blacklists(self, request: operations.ListBlacklistsRequest) -> operations.ListBlacklistsResponse:
        r"""List matchlists
        Returns an array of matchlist in your environment. 
        
        Because the response is paginated, the request body has a `limit` and `offset` field. At least one must be filled.
        * `limit`  indicates how many objects the request returns (the page maximum is 50)
        * `offset` indicates the offset for pagination. An `offset` value of 1 starts with the environment's first record.
        
        The `total_count` field contains the total number of matchlists where the  `response_count` field contains the number of matchlists included in the response.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/blacklists/list"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ListBlacklistsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListBlacklistResponse])
                res.list_blacklist_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListBlacklistsMessageGeneralResponse])
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

    