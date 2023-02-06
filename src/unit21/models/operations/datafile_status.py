import dataclasses



@dataclasses.dataclass
class DatafileStatusPathParams:
    file_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'file_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DatafileStatusRequest:
    path_params: DatafileStatusPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DatafileStatusResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    