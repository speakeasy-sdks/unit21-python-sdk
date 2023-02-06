import requests
from . import utils
from typing import Optional
from unit21.models import operations, shared

class CasesAPI:
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

    
    def create_case(self, request: operations.CreateCaseRequest) -> operations.CreateCaseResponse:
        r"""Create a case
        Creates a new case, sending case data in the request body. 
        To create a case, you MUST include the following fields: `case_id`, `title`, and `created_at`.  The other top-level fields are optional.
        
        If we receive a request to create a case for an `case_id` that already exists in our system,  we will respond with a **409 error code** indicating that this case cannot be created/updated. You must use the `/case/update` endpoint to update a case.
        
        You can add the following objects to a case:
        
          | Field                    | Type     | Description                                                             |
          |--------------------------|----------|-------------------------------------------------------------------------|
          | `alerts`	               | Array[]  | Alerts that are associated with this case. Consists of `alert_id`s      |
          | `events`	               | Array[]  | Transactions affiliated with the case. Consists of `event_id`s          |
          | `entities`	             | Array[]  | Entities affiliated with the case. Consists of `entity_id`s             |
        
        Updates to a cases's `case_id` are not allowed.
        
        Follow the links for more information:
          - [Endpoint options](https://docs.unit21.ai/reference/endpoint-options)
          - [Batch uploads](https://docs.unit21.ai/reference/batch-request-examples)
          - [Modifying tags](https://docs.unit21.ai/reference/modifying-tags)
        
        
        The response will consist of the following fields:
        
          | Field                    | Type     | Description                                          |
          |--------------------------|----------|------------------------------------------------------|
          | `case_id`	               | String   | 	Unique identifier of the case on your platform     |
          | `previously_existed`	   | Boolean  | 	If case (with the same `case_id`) already exists   |
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/cases/create"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateCaseResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.create_case_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.CreateCaseMessageGeneralResponse])
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

    
    def export_cases(self, request: operations.ExportCasesRequest) -> operations.ExportCasesResponse:
        r"""Bulk export cases
        Initiates an email and dashboard export of cases. The export will be as a CSV file.
        
        Either the agent `ID` or `email` is required to begin the export.
        
        Either the `filters` or the list of `case IDs` are required for the export.
        
        Custom data filters are not supported for bulk exports at this time.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/cases/bulk-export"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ExportCasesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.BulkExportResponse])
                res.bulk_export_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ExportCasesMessageGeneralResponse])
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

    
    def get_case_by_unit21_id(self, request: operations.GetCaseByUnit21IDRequest) -> operations.GetCaseByUnit21IDResponse:
        r"""Get a case
        Returns all data objects belonging to a single case.
        
        This endpoint requires the `unit21_id` which is a unique ID created by Unit21 when the case is first created.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/cases/{unit21_id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetCaseByUnit21IDResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.case_list = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCaseByUnit21IDMessageGeneralResponse])
                res.message_general_response = out

        return res

    
    def link_media_to_case(self, request: operations.LinkMediaToCaseRequest) -> operations.LinkMediaToCaseResponse:
        r"""Add media to a case
        Adds rich media objects (images, videos, etc.) to an existing case. 
        
        This endpoint is useful for sending in rich media such as profile pictures, ID card scans, official documents etc.  that you want available for investigative and verification purposes.
        
        Supported file types are: txt, pdf, video (mp4, mov, wmv, avi, mkv), images (png, jpg, tiff, gif, raw, eps).
        
        The payload to this endpoint can either be a **form-data** or a **base64** encoded media file via the requests JSON body.
        
        **Form-data** sent to this endpoint must use the key `media_key` and the `value` as the media file.  If you wish to provide optional information, use the `media_key` and provide stringified JSON data as the value.  There are no required fields in each media file's supplementary form data. However, if a recognized `media_type` value is provided,  the Unit21 system will be able to use the media object for purposes such as document verification.
        
        ```
            --form 'document_front=@/src/103031/images/document_front.jpg' \
            --form 'document_front={\"media_type\": \"IMAGE_ID_CARD_FRONT\", \"source\": \"passport_app\", \"timestamp\": 1572673229}'
        ```
        
        **Base64** encoded media objects must follow the format:
        
        ```json
          {
            \"media\": \"iVBORw0KGgoAAAANSUhEUgAAAQMAAADCCAYAAABNEqduAAAgAElEQVR4Aey9CbgmV1Xv...\",
            \"name\": \"Drivers_License.png\",
            \"media_type\": \"IMAGE_DRIVERS_LICENSE_FRONT\"
          }
        ```
            
        `media` and `name` are the only required fields for each media object. The `name`` must include the file extension such a `File.pdf`. Supplementary form data is sent through the optional `custom_data` object.
        
        Recognized values of `media_type` are: 
        
          | media_type                    |
          |-------------------------------|
          | IMAGE_PROFILE_PICTURE         |
          | IMAGE_DRIVERS_LICENSE_FRONT   |
          | IMAGE_DRIVERS_LICENSE_BACK    |
          | IMAGE_PASSPORT_FRONT          |
          | IMAGE_ID_CARD_FRONT           |
          | IMAGE_ID_CARD_BACK            |
          | IMAGE_FACE_IMAGE              |
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/cases/{unit21_id}/link-media", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PUT", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.LinkMediaToCaseResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
        elif r.status_code == 400:
            pass
        elif r.status_code == 401:
            pass
        elif r.status_code == 403:
            pass
        elif r.status_code == 404:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.error_response = out
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

    
    def list_cases(self, request: operations.ListCasesRequest) -> operations.ListCasesResponse:
        r"""List cases
        Returns an array of top-level information about cases in your environment.
        
        Because the response is paginated, the request body has a `limit` and `offset` field. At least one must be filled.
        * `limit`  indicates how many objects the request returns (the page maximum is 50)
        * `offset` indicates the offset for pagination. An `offset` value of 1 starts with the environment's first record.
        
        To narrow down your case search, we provide filter parameters to this endpoint. Note that all list inputs function as an \"or\" filter, as in any one of the values must match the selected case(s):
        
        
          | Field                   | Type        | Description                                                                                                       |
          | ----------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------- |
          | `created_after`         | Numeric     | Cases created on or after this unix timestamp                                                                     |
          | `created_before`        | Numeric     | Cases created before this unix timestamp                                                                          |
          | `dispositions`          | String[]    | List of case disposition states (defined on an integration basis)                                                 |
          | `dispositioned_after`   | Numeric     | Cases with a disposition most recently updated after this unix timestamp                                          |
          | `dispositioned_before`  | Numeric     | Cases with a disposition most recently updated before this unix timestamp                                         |
          | `dispositioned_by`      | String[]    | List of agent emails. Returns alerts with a disposition most recently changed by agents in the list               |
          | `rules`                 | Numeric[]   | List of Unit21 rule ids that are associated with the case                                                         |
          | `associated_entities`   | Numeric[]   | List of Unit21 entity ids associated with this case                                                               |
          | `associated_events`     | Numeric[]   | List of Unit21 event ids associated with this case                                                                |
          | `associated_alerts`     | Numeric[]   | List of Unit21 alert ids associated with this case                                                                |
          | `sources`               | String[]    | Must be list of alert sources: `INTERNAL`, `EXTERNAL`                                                             |
          | `statuses`              | String[]    | Must be list of alert statuses: `OPEN`, `CLOSED`                                                                  |
          | `tag_filters`           | String[]    | List of string tags (`key:value`) or keys to associate this case with (e.g. `case_type:high_velocity` or `case_type`). If only the key is provided, we will match against all tags with that key        |
          | `limit`                 | Numeric     | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10          |
          | `offset`                | Numeric     | The offset for pagination. Default is 1                                                                           |
          | `options`               | Object      | Options for the data included in the returned cases. Removing unneeded options can improve response speed         |
        
        
        The `total_count` field contains the total number of case where the  `response_count` field contains the number of cases included in the response.
        
        Follow the links for more information:
          - [Endpoint options](https://docs.unit21.ai/reference/endpoint-options)
          
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/cases/list"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ListCasesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListCaseResponse])
                res.list_case_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListCasesMessageGeneralResponse])
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

    
    def update_case(self, request: operations.UpdateCaseRequest) -> operations.UpdateCaseResponse:
        r"""Update case
        Update a case through its `unit21_id`. ONLY EXTERNAL CASES CAN BE UPDATED!
            
        
        Updating a case has no required fields. You MAY send any subset of the fields that the `cases/create` endpoint accepts.
        
        This endpoint requires the `unit21_id` which is a unique ID created by Unit21 when the case is first created.
        
        Note that you can also update an alert using an upsert through `/cases/create`.
        
        Follow the links for more information:
          - [Endpoint options](https://docs.unit21.ai/reference/endpoint-options)
          - [Custom data](https://docs.unit21.ai/reference/best-practices-for-custom-data)
          - [Batch uploads](https://docs.unit21.ai/reference/batch-request-examples)
          - [Modifying tags](https://docs.unit21.ai/reference/modifying-tags)
        
        
        The response will consist of the following fields:
        
          | Field                    | Type     | Description                                          |
          |--------------------------|----------|------------------------------------------------------|
          | `case_id`	               | String   | 	Unique identifier of the case on your platform     |
          | `previously_existed`	   | Boolean  | 	If entity (with the same `case_id`) already exists |
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/cases/{unit21_id}/update", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PUT", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateCaseResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.update_case_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.UpdateCaseMessageGeneralResponse])
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

    