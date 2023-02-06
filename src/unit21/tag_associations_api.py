import requests
from . import utils
from typing import Optional
from unit21.models import operations, shared

class TagAssociationsAPI:
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

    
    def list_tags(self, request: operations.ListTagsRequest) -> operations.ListTagsResponse:
        r"""List tags
        Returns an array of objects associated with a set of tags in your environment.     
        
        Because the response is paginated, the request body has a `limit` and `offset` field. At least one must be filled.
        * `limit`  indicates how many objects the request returns (the page maximum is 1000)
        * `offset` indicates the offset for pagination. An `offset` value of 1 starts with the environment's first record.
        
        To narrow down your tag association search, we provide filter parameters to this endpoint.
        
          | Field                   | Type        | Description                                                                                                       |
          | ----------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------- |
          | `created_after`         | Numeric     | Tag associations created on or after this unix timestamp                                                          |
          | `created_before`        | Numeric     | Tag associations created before this unix timestamp                                                               |
          | `object_types`          | String[]    | List of object types to match against. Supported values are `alert`, `case`, `sar`, `rule`, `agent`, `event`, `entity`, and `instrument`. Specifying [`entity`, `alert`] means that we will only match against tags associated with entities and alerts in the system, and will not return results of tags associated with rules, events etc. If more than one value is provided to `object_types` and `object_id` is specified, an error will be thrown.     |
          | `object_id`             | String      | String representing the unit21 ID of the object you want to get tag associations for. If this is specified and `object_types` contains more than one value, an error will be thrown.                    |
          | `tag_filters`           | String[]    | List of string tags (`key:value`) or keys to associate this case with (e.g. `case_type:high_velocity` or `case_type`). If only the key is provided, we will match against all tags with that key        |
          | `limit`                 | Numeric     | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10          |
          | `offset`                | Numeric     | The offset for pagination. Default is 1                                                                           |
          | `options`               | Object      | Options for the data included in the returned cases. Removing unneeded options can improve response speed         |
        
        
        The `total_count` field contains the total number of tags where the  `response_count` field contains the number of tags included in the response.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/tag-associations/list"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ListTagsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListTagResponse])
                res.list_tag_response = out
        elif r.status_code == 400:
            pass
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

    