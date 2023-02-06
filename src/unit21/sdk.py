
import requests
from . import utils
from .agents_api import AgentsAPI
from .alerts_api import AlertsAPI
from .cases_api import CasesAPI
from .datafiles_api import DatafilesAPI
from .entities_api import EntitiesAPI
from .entity_verification_api import EntityVerificationAPI
from .events_api import EventsAPI
from .exports_api import ExportsAPI
from .import_api import ImportAPI
from .instruments_api import InstrumentsAPI
from .matchlists_api import MatchlistsAPI
from .rules_api import RulesAPI
from .sars_api import SarsAPI
from .tag_associations_api import TagAssociationsAPI
from .verification_forms_api import VerificationFormsAPI
from .webhooks_api import WebhooksAPI
from unit21.models import shared

SERVERS = [
	"https://sandbox1-api.unit21.com/v1",
	"https://sandbox2-api.unit21.com/v1",
	"https://api.unit21.com/v1",
	"https://api.prod2.unit21.com/v1",
]


class Unit21:
    
    agents_api: AgentsAPI
    alerts_api: AlertsAPI
    cases_api: CasesAPI
    datafiles_api: DatafilesAPI
    entities_api: EntitiesAPI
    entity_verification_api: EntityVerificationAPI
    events_api: EventsAPI
    exports_api: ExportsAPI
    import_api: ImportAPI
    instruments_api: InstrumentsAPI
    matchlists_api: MatchlistsAPI
    rules_api: RulesAPI
    sars_api: SarsAPI
    tag_associations_api: TagAssociationsAPI
    verification_forms_api: VerificationFormsAPI
    webhooks_api: WebhooksAPI

    _client: requests.Session
    _security_client: requests.Session
    _security: shared.Security
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "2.1.0"
    _gen_version: str = "1.0.0"

    def __init__(self) -> None:
        self._client = requests.Session()
        self._security_client = requests.Session()
        self._init_sdks()


    def config_server_url(self, server_url: str, params: dict[str, str]):
        if params is not None:
            self._server_url = utils.replace_parameters(server_url, params)
        else:
            self._server_url = server_url

        self._init_sdks()
    

    def config_client(self, client: requests.Session):
        self._client = client
        
        if self._security is not None:
            self._security_client = utils.configure_security_client(self._client, self._security)
        self._init_sdks()
    

    def config_security(self, security: shared.Security):
        self._security = security
        self._security_client = utils.configure_security_client(self._client, security)
        self._init_sdks()
    
    
    def _init_sdks(self):
        
        self.agents_api = AgentsAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.alerts_api = AlertsAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.cases_api = CasesAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.datafiles_api = DatafilesAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.entities_api = EntitiesAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.entity_verification_api = EntityVerificationAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.events_api = EventsAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.exports_api = ExportsAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.import_api = ImportAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.instruments_api = InstrumentsAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.matchlists_api = MatchlistsAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.rules_api = RulesAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.sars_api = SarsAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.tag_associations_api = TagAssociationsAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.verification_forms_api = VerificationFormsAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.webhooks_api = WebhooksAPI(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
    
    