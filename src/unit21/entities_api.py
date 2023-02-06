import requests
from . import utils
from typing import Optional
from unit21.models import operations, shared

class EntitiesAPI:
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

    
    def add_instruments(self, request: operations.AddInstrumentsRequest) -> operations.AddInstrumentsResponse:
        r"""Add instruments to entity
        Associate an entity with an array of instruments.
        
        Specify the `instrument_id` of the instrument when associating instruments.
        
        [Placeholder](https://docs.unit21.ai/reference/placeholder-objects) entities cannot be updated.
        
        If we do not find any instruments with a corresponding `instrument_id` in our system, we will create a [placeholder](https://docs.unit21.ai/reference/placeholder-objects) for it.
        
        Instrument details can then be supplemented through the `/instruments/create` or `/instruments/update` endpoints.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/{org_name}/entities/{entity_id}/add-instruments", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PUT", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.AddInstrumentsResponse(status_code=r.status_code, content_type=content_type)
        
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

    
    def create_entity(self, request: operations.CreateEntityRequest) -> operations.CreateEntityResponse:
        r"""Create an entity
        Creates a new entity, sending entity data in the request body. 
        
        If the `/entities/create` API is called for an entity that already exists in our system, it is treated it as an  [upsert](https://docs.unit21.ai/reference/should-i-update-or-upsert) and an update on the existing entity is performed. The response to the request will then contain the entry `previously_existed: true`. 
        
        Unit21 selectively ignores upserts if the request is identical to a previous request. The response to any  ignored upsert will contain the field `ignored: true`. 
        
        If you want to perform strict validation and not perform an upsert on conflict, specifying  `options.upsert_on_conflict: false` will result in the API responding with a **409 error code** indicating  that this entity cannot be overwritten.
        
        To turn a [placeholder](https://docs.unit21.ai/reference/placeholder-objects) entity into an entity in the Unit21 system, use this endpoint.
        
        Whitelisted entities cannot be updated through the `/entities/create` endpoint. 
        
        Updates to an entity's `general_data.entity_id` are not allowed.  
        
        Instruments can be associated with entities by providing the IDs of these  instruments within the `instrument_ids` section of the request. If the instrument doesn't already exist,  Unit21 creates a [placeholder](https://docs.unit21.ai/reference/placeholder-objects) instrument.
        
        We recommend that you create entities prior to running verification. In the event you wish to run a  verification on an entity immediately, Unit21 recommends that you wait at-least 2 minutes for your entity  data to be fully processed. You will receive a **423 error code** if an entity is *busy*. When a 200 response is received,  the data has been successfully stored on the Unit21 backend; however, it may take a few additional seconds to process that data  so that it becomes available in subsequent API calls, in the frontend UI, and/or for verification purposes.
        
        Follow the links for more information:
          - [Relationships](https://docs.unit21.ai/reference/relationships)
          - [Endpoint options](https://docs.unit21.ai/reference/endpoint-options)
          - [Verification options](https://docs.unit21.ai/reference/identity-verification-options)
          - [Custom data](https://docs.unit21.ai/reference/best-practices-for-custom-data)
          - [Batch uploads](https://docs.unit21.ai/reference/batch-request-examples)
          - [Modifying tags](https://docs.unit21.ai/reference/modifying-tags)
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/entities/create"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateEntityResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.create_entity_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.CreateEntityMessageGeneralResponse])
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

    
    def create_entity_directly(self, request: operations.CreateEntityDirectlyRequest) -> operations.CreateEntityDirectlyResponse:
        r"""Create an entity directly
        Creates or updates an entity immediately, publishing directly to kafka. This is a performance endpoint.
        
        Please see the `/entity/create` [endpoint](https://docs.unit21.ai/reference/create_entity) for more information.
        
        A successfull entry comes back `null`.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/entities/create/direct"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateEntityDirectlyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
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

    
    def del_media_entity(self, request: operations.DelMediaEntityRequest) -> operations.DelMediaEntityResponse:
        r"""Delete entity media
        Deletes all rich media objects (images, videos, etc.) belonging to an existing entity. 
        
        [Placeholder](https://docs.unit21.ai/reference/placeholder-objects) entities cannot be updated.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/{org_name}/entities/{entity_id}/delete-all-media", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("PUT", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DelMediaEntityResponse(status_code=r.status_code, content_type=content_type)
        
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

    
    def export_entities(self, request: operations.ExportEntitiesRequest) -> operations.ExportEntitiesResponse:
        r"""Bulk export entities
        Initiates an email and dashboard export of entities. The export will be as a CSV file.
        
        [Placeholder](https://docs.unit21.ai/reference/placeholder-objects) entities are not exported.
        
        Either the `filters` or the list of `entity_ids` are required for the export. 
        
        **Currently `entity_ids` should actually be `unit21_ids`.**
        
        Custom data filters are not supported for bulk exports at this time.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/entities/bulk-export"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ExportEntitiesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.message_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ExportEntitiesMessageGeneralResponse])
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

    
    def get_entity(self, request: operations.GetEntityRequest) -> operations.GetEntityResponse:
        r"""Get an entity
        Returns all data objects belonging to a single entity, including `general_data`, `document_data`, etc.
        
        [Placeholder](https://docs.unit21.ai/reference/placeholder-objects) entities will not be listed.
        
        This endpoint requires the `entity_id` which is a unique ID created by your organization to identify the entity. The `org_name` is your Unit21 appointed organization name such as `google` or `acme`.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/{org_name}/entities/{entity_id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetEntityResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.entity_list = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetEntityMessageGeneralResponse])
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

    
    def link_media_to_entity(self, request: operations.LinkMediaToEntityRequest) -> operations.LinkMediaToEntityResponse:
        r"""Add media to an entity
        Adds rich media objects (images, videos, etc.) to an existing entity. 
        
        [Placeholder](https://docs.unit21.ai/reference/placeholder-objects) entities cannot be updated.
        
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
            \"media_type\": \"IMAGE_DRIVERS_LICENSE_FRONT\",
            \"custom_data\": {
              \"internal_notes\": \"Reviewed by Mitchell on 31 June 2019\",
              \"reviewers\": 3,
              \"login\": 1638384860,
              \"timestamp\": \"2012-03-40 05:12:41.000Z\",
              \"daily_email\": true,
              \"employees\": [\"John\", \"Anna\", \"Peter\"],
              \"socure_device_session_id\": \"12121212121212112\"
            }
          }
        ```
        
        `media` and `name` are the only required fields for each media object. The `name` must include the file extension such a `File.pdf`. Supplementary form data is sent through the optional `custom_data` object.
        
        For verification purposes, recognized values of `media_type` are: 
        
        
          | media_type                  |
          |-----------------------------|
          | IMAGE_PROFILE_PICTURE       |
          | IMAGE_DRIVERS_LICENSE_FRONT |
          | IMAGE_DRIVERS_LICENSE_BACK  |
          | IMAGE_PASSPORT_FRONT        |
          | IMAGE_ID_CARD_FRONT         |
          | IMAGE_ID_CARD_BACK          |
          | IMAGE_FACE_IMAGE            | 
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/{org_name}/entities/{entity_id}/link-media", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PUT", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.LinkMediaToEntityResponse(status_code=r.status_code, content_type=content_type)
        
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

    
    def list_entities(self, request: operations.ListEntitiesRequest) -> operations.ListEntitiesResponse:
        r"""List entities
        Returns paginated list of of top-level information about entities. 
        
        [Placeholder](https://docs.unit21.ai/reference/placeholder-objects) entities are not listed.
        
        Because the response is paginated, the request body has a `limit` and `offset` field. At least one must be filled.
        * `limit`  indicates how many objects the request returns (the page maximum is 50)
        * `offset` indicates the offset for pagination. An `offset` value of 1 starts with the environment's first record. The offset is relative to the number of pages (not the total count of objects).
        * `case_id`  is a filter. Only entities with the associated case ID will be shown.
        * `alert_id` is a filter. Only entities with the associated alert ID will be shown.
        
        The `total_count` field is set to 0. Please call this paginated endpoint, increasing the offset,  until you receive fewer than the maximum number of objects per call.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/entities/list"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ListEntitiesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListEntityResponse])
                res.list_entity_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListEntitiesMessageGeneralResponse])
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

    
    def update_entity(self, request: operations.UpdateEntityRequest) -> operations.UpdateEntityResponse:
        r"""Update entity
        Updates an entity's information using the `entity_id` from your platform. 
        
        Updating an entity has no required fields. You MAY send any  subset of the fields that the entities/create endpoint accepts.
        
        [Placeholder](https://docs.unit21.ai/reference/placeholder-objects) entities cannot be updated.
        
        This endpoint requires the `entity_id` which is a unique ID created by your organization to identify the entity. The `org_name` is your Unit21 appointed organization name such as `google` or `acme`.
        
        Note that you can also update an entity using an upsert through `/entities/create`.
        
        Follow the links for more information:
          - [Relationships](https://docs.unit21.ai/reference/relationships)
          - [Endpoint options](https://docs.unit21.ai/reference/endpoint-options)
          - [Verification options](https://docs.unit21.ai/reference/identity-verification-options)
          - [Custom data](https://docs.unit21.ai/reference/best-practices-for-custom-data)
          - [Batch uploads](https://docs.unit21.ai/reference/batch-request-examples)
          - [Modifying tags](https://docs.unit21.ai/reference/modifying-tags)
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/{org_name}/entities/{entity_id}/update", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._security_client
        
        r = client.request("PUT", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateEntityResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.update_entity_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.UpdateEntityMessageGeneralResponse])
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

    