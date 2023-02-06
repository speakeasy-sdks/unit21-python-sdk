import requests
from . import utils
from unit21.models import operations

class ImportAPI:
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

    
    def datafile_status(self, request: operations.DatafileStatusRequest) -> operations.DatafileStatusResponse:
        r"""Retrieve datafile status
        Retrieve datafile status.
        
        Note `file_id` will be included in the initial request to get a presigned_url.
        
        Programmatically check on the status of files and take action should errors occur.
        
        Files uploaded and processed have the following `status` value with the following definitions:
        
          | Error code               | Definition                                                                                                                                 |
          |--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
          | `PENDING_UPLOAD`	       | Customer is programmatically uploading via API, but the file has not landed (or not yet been detected as landed) in S3                     |
          | `ADDED`	                 | Customer manually uploaded to the UI, but has not attempted to process the file yet                                                        |
          | `QUEUED`	               | File is in a queue waiting to process                                                                                                      |
          | `PROCESSING`	           | File is presently being processed                                                                                                          |
          | `FINISHED`	             | The File finished successfully. Note that this does not mean all data is processed successfully as referenced by Hard error Handling below |
          | `FAILED`	               | File hit a hard failure case and was unable to process data                                                                                |
        
        
        Hard errors refer to unprocessable datafiles, aka files that whose status end up `FAILED` are accompanied by an error code from this list:
        
          | Error code               | Definition                                                                                                                                                                                                                                           |
          |--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
          | `unparseable_file`	     | File failed to read (i.e. file contents was not actually csv or the contents use a non-traditional delimiter character)                                                                                                                              |
          | `invalid_schema`	       | By the stream configuration, the file had unexpected column headers or values present and thus the system did not process the data                                                                                                                   |
          | `stream_not_configured`	 | This error means that the stream has not yet been configured with all the necessary settings to ingest the data yet. Generally this should only happen if you are testing uploaded datafiles in advance of having defined landing the data in Unit21 |
          | `unknown`	               | This is akin to 500 server error, and Unit21 does not have a specific known cause at this time                                                                                                                                                       |
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/imports/{file_id}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DatafileStatusResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def get_pre_signed_url(self, request: operations.GetPreSignedURLRequest) -> operations.GetPreSignedURLResponse:
        r"""Get pre-signed URL
        Get details your unique URL you can use to import data into the Unit21 system.
        
        The response will include a URL which you must use to upload your datafile. In the example below, your datafile will be uploaded to https://local-tm-uploads.s3.amazonaws.com/.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/imports/pre-signed-url/create"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.GetPreSignedURLResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def list_datafiles(self, request: operations.ListDatafilesRequest) -> operations.ListDatafilesResponse:
        r"""Retrieve datafiles list
        Retrieve list of datafiles.
        
        Note `file_id` will be included in the initial request to get a presigned_url.
        
        This route will be limited to 1000 records ordered by upload time.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/imports/list"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ListDatafilesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def upload_datafiles(self, request: operations.UploadDatafilesRequest) -> operations.UploadDatafilesResponse:
        r"""Upload data to URL
        Upload your file to our S3 bucket using the pre signed AWS URL you received in the `create` endpoint.
        
        **PLEASE NOTE THAT THE URL FOR THIS POST REQUEST IS THE `pre_signed_url` ONLY.** YOU MUST REMOVE `https://sandbox1-api.unit21.com/v1`.
        
        Documentation shows an incorrect example: https://sandbox1-api.unit21.com/v1/local-tm-uploads.s3.amazonaws.com/.
        
        The correct URL would be: https://local-tm-uploads.s3.amazonaws.com/
        
        Only one file can be uploaded in a request, with a file size maximum of 1GB. Please add a waiting time of two seconds between requests.
        
        Use `--form file` to specify the file.
        
        We support JSON, JSONL, CSV format only.
        
        """
        
        base_url = operations.UPLOAD_DATAFILES_SERVERS[0]
        if request.server_url is not None:
            base_url = request.server_url
        
        
        url = utils.generate_url(base_url, "/{pre_signed_url}", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UploadDatafilesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    