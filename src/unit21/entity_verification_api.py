import requests
from . import utils
from typing import Optional
from unit21.models import operations, shared

class EntityVerificationAPI:
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

    
    def add_verification_result_to_entity(self, request: operations.AddVerificationResultToEntityRequest) -> operations.AddVerificationResultToEntityResponse:
        r"""Link external verification
        Add the verification result from an external ID provider to an entity on the Unit21 system.
        You can only send 1 result per request.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/entities/{unit21_id}/link-verification-result", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.AddVerificationResultToEntityResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.link_verification_response = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.AddVerificationResultToEntityMessageGeneralResponse])
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

    
    def get_entity_verification_workflow_executions(self, request: operations.GetEntityVerificationWorkflowExecutionsRequest) -> operations.GetEntityVerificationWorkflowExecutionsResponse:
        r"""Get entity verification workflow IDs
        Returns the verification workflow IDs for an entity.
        
        This endpoint requires the `unit21_id` which is a unique ID created by Unit21 when the entity is first created.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/entities/{unit21_id}/verification_workflow_executions", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetEntityVerificationWorkflowExecutionsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[shared.VerificationList]])
                res.verification_list = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetEntityVerificationWorkflowExecutionsMessageGeneralResponse])
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

    
    def get_verification_result(self, request: operations.GetVerificationResultRequest) -> operations.GetVerificationResultResponse:
        r"""Get verification results by result id
        Returns all the information from the verification of a specific entity.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/verification/result/{result_id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetVerificationResultResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.VerificationResult])
                res.verification_result = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetVerificationResultMessageGeneralResponse])
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

    
    def get_verification_result_from_workflow_execution(self, request: operations.GetVerificationResultFromWorkflowExecutionRequest) -> operations.GetVerificationResultFromWorkflowExecutionResponse:
        r"""Get verification results from workflow
        Returns all the information from the verification workflow execution for a specific entity.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/verification/verification-workflow-execution/{verification_workflow_execution_id}/results", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetVerificationResultFromWorkflowExecutionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[shared.VerificationResultList]])
                res.verification_result_list = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetVerificationResultFromWorkflowExecutionMessageGeneralResponse])
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

    
    def get_verification_workflow_execution(self, request: operations.GetVerificationWorkflowExecutionRequest) -> operations.GetVerificationWorkflowExecutionResponse:
        r"""Get verification workflow execution details
        Returns all the data associated with a verification_workflow_execution_id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/verification/verification-workflow-execution/{verification_workflow_execution_id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetVerificationWorkflowExecutionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.verification = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetVerificationWorkflowExecutionMessageGeneralResponse])
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

    
    def run_verifications_workflow_through_external_id(self, request: operations.RunVerificationsWorkflowThroughExternalIDRequest) -> operations.RunVerificationsWorkflowThroughExternalIDResponse:
        r"""Verify an entity
        Run a verification workflow on an entity using the `entity_id` from your platform. 
        
        Requires a `workflow_id`. You can create a verification workflow from the Unit21 dashboard.
        
        This endpoint requires the `entity_id` which is a unique ID created by your organization to identify the entity. The `org_name` is your Unit21 appointed organization name such as `google` or `acme`.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/{org_name}/entities/{entity_id}/verify", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.RunVerificationsWorkflowThroughExternalIDResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.RunVerificationsWorkflowThroughExternalID200ApplicationJSON])
                res.run_verifications_workflow_through_external_id_200_application_json_object = out
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.RunVerificationsWorkflowThroughExternalIDMessageGeneralResponse])
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

    
    def update_continuous_monitoring(self, request: operations.UpdateContinuousMonitoringRequest) -> operations.UpdateContinuousMonitoringResponse:
        r"""Update continuous monitoring
        Fetch status and enables/disables Socure continuous monitoring for an entity.
        
        For asynchronous continuous monitoring, the endpoint will always return a 200 success status response.
        
        For synchronous continous monitoring, the endpoint will always return a 200 success status response  but you should look at the `is_success = true` field to check if the result was actually successful: 
        
        `
          {
            \"error_message\": \"This entity has no existing continuous monitoring subscriptions to disable.\",
            \"is_success\": true
          }
        `
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/entities/{unit21_id}/continuous-monitoring", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateContinuousMonitoringResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.UpdateContinuousMonitoringMessageGeneralResponse])
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

    
    def update_suppressed_provider_entities(self, request: operations.UpdateSuppressedProviderEntitiesRequest) -> operations.UpdateSuppressedProviderEntitiesResponse:
        r"""Suppress provider entity
        Mute Socure continuous monitoring for an entity. 1 - Suppress 0 - Unsuppress
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/entities/{unit21_id}/suppress-provider-entity", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateSuppressedProviderEntitiesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
        elif r.status_code == 400:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.UpdateSuppressedProviderEntitiesMessageGeneralResponse])
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

    