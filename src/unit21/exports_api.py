import requests
from . import utils
from typing import Optional
from unit21.models import operations, shared

class ExportsAPI:
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

    
    def download_file_export(self, request: operations.DownloadFileExportRequest) -> operations.DownloadFileExportResponse:
        r"""Download export
        Returns a signed url to download the file.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/file-exports/download/{file_export_id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DownloadFileExportResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListExportURLResponse])
                res.list_export_url_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.DownloadFileExportMessageGeneralResponse])
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

    
    def list_exports(self, request: operations.ListExportsRequest) -> operations.ListExportsResponse:
        r"""List exports
        Returns paginated list exports. It will only show the exports initiated by the requester (The requester is the creator of the API key)
        
        **This endpoint omits any exports from the \"System\" source (generated directly from the Dashboard instead of the API).**
        
        Because the response is paginated, the request body has a `limit` and `offset` field. At least one must be filled.
        * `limit`  indicates how many objects the request returns (the page maximum is 50)
        * `offset` indicates the offset for pagination. An `offset` value of 1 starts with the environment's first record. The offset is relative to the number of pages (not the total count of objects).
        
        The `total_count` field contains the total number of exports where the  `response_count` field contains the number of exports included in the response.
        
        The `statuses` for exports address:
        
          | Status                   | Description                                             |
          |--------------------------|---------------------------------------------------------|
          | READY_FOR_DOWNLOAD	     | File is ready for download                              |
          | GENERATING	             | File is generating                                      |
          | FAILED                   | File export failed                                      |
          | REQUESTED	               | File exort has been requested                           |
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/file-exports/list"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ListExportsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListExportResponse])
                res.list_export_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListExportsMessageGeneralResponse])
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

    