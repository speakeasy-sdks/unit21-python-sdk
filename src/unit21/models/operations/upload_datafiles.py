import dataclasses
from typing import Optional


UPLOAD_DATAFILES_SERVERS = [
	"https://api.unit21.com",
]


@dataclasses.dataclass
class UploadDatafilesPathParams:
    pre_signed_url: str = dataclasses.field(metadata={'path_param': { 'field_name': 'pre_signed_url', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UploadDatafilesRequestBodyFile:
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    file: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'file' }})
    

@dataclasses.dataclass
class UploadDatafilesRequestBody:
    file: Optional[UploadDatafilesRequestBodyFile] = dataclasses.field(default=None, metadata={'multipart_form': { 'file': True }})
    

@dataclasses.dataclass
class UploadDatafilesRequest:
    path_params: UploadDatafilesPathParams = dataclasses.field()
    request: Optional[UploadDatafilesRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    server_url: Optional[str] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class UploadDatafilesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    