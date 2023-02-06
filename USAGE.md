<!-- Start SDK Example Usage -->
```python
import unit21
from unit21.models import operations, shared

s = unit21.Unit21()
s.config_security(
    security=shared.Security(
        api_key_auth=shared.SchemeAPIKeyAuth(
            api_key="YOUR_API_KEY_HERE",
        ),
    )
)
   
req = operations.DeactivateAgentRequest(
    path_params=operations.DeactivateAgentPathParams(
        agent_email="unde",
    ),
)
    
res = s.agents_api.deactivate_agent(req)

if res.agent_list is not None:
    # handle response
```
<!-- End SDK Example Usage -->