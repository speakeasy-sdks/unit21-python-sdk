# Python SDK for Unit21 API

[Unit21](https://docs.unit21.ai/docs) is an anti-money laundering (AML) and Fraud system that runs securely in your browser. Unit21 provides:

* Identity Verification - find suspicious parties (KYB/KYC) and monitor them
* Transaction Monitoring - create rules to find fraudulent transactions
* Case Management - investigate potential offenders and suspicious transactions
* Report Filing and Actionable Webhooks - report offenders to the authorities or ban them

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install unit21api
```
<!-- End SDK Installation -->

## Authentication 

The Unit21 API uses API keys to authenticate requests. These API keys can be generated within the dashboard and must be supplied with each request.

Your API keys can be used to perform a variety of actions against the API; whilst GET requests do not affect data in your account, the PATCH and POST requests can create, alter and reassign searches - so please ensure you follow best practice for managing API keys.

Please remember to:

Keep your keys secure
Rotate your API keys on a frequent basis
Never store your API keys in a publicly-accessible location
When making requests to the Unit21 API the key must be provided in the header:

```bash
curl -X POST \
    -H 'Content-Type: application/json' \
    -H 'u21-key: YOUR_API_KEY' \
    -d '{
            "request_body": "..."
        }' \
    https://<API_ENDPOINT>/<path>
```

## SDK Example Usage
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

<!-- Start SDK Available Operations -->
## SDK Available Operations


### agents_api

* `deactivate_agent` - Deactivate an agent
* `list_agents` - List agents

### alerts_api

* `create_alert` - Create alerts
* `export_alerts` - Bulk export alerts
* `get_alert_by_unit21_id` - Get an alert
* `link_media_to_alert` - Add media to an alert
* `list_alerts` - List alerts
* `update_alert` - Update alert

### cases_api

* `create_case` - Create a case
* `export_cases` - Bulk export cases
* `get_case_by_unit21_id` - Get a case
* `link_media_to_case` - Add media to a case
* `list_cases` - List cases
* `update_case` - Update case

### datafiles_api

* `create_datafiles` - Upload datafiles
* `get_datafile_by_unit21_id` - Get datafile
* `get_datafile_mappings` - Retrieve datafile mappings

### entities_api

* `add_instruments` - Add instruments to entity
* `create_entity` - Create an entity
* `create_entity_directly` - Create an entity directly
* `del_media_entity` - Delete entity media
* `export_entities` - Bulk export entities
* `get_entity` - Get an entity
* `link_media_to_entity` - Add media to an entity
* `list_entities` - List entities
* `update_entity` - Update entity

### entity_verification_api

* `add_verification_result_to_entity` - Link external verification
* `get_entity_verification_workflow_executions` - Get entity verification workflow IDs
* `get_verification_result` - Get verification results by result id
* `get_verification_result_from_workflow_execution` - Get verification results from workflow
* `get_verification_workflow_execution` - Get verification workflow execution details
* `run_verifications_workflow_through_external_id` - Verify an entity
* `update_continuous_monitoring` - Update continuous monitoring
* `update_suppressed_provider_entities` - Suppress provider entity

### events_api

* `create_event` - Create an event
* `export_events` - Bulk export events
* `export_transactions` - Bulk export transactions
* `get_event` - Get an event
* `list_events` - List events
* `update_event` - Update event

### exports_api

* `download_file_export` - Download export
* `list_exports` - List exports

### import_api

* `datafile_status` - Retrieve datafile status
* `get_pre_signed_url` - Get pre-signed URL
* `list_datafiles` - Retrieve datafiles list
* `upload_datafiles` - Upload data to URL

### instruments_api

* `create_instrument` - Create an instrument
* `export_instruments` - Bulk export instruments
* `get_instrument` - Get an instrument
* `list_instruments` - List instruments
* `update_instrument` - Update instrument

### matchlists_api

* `add_blacklist_values` - Add items to a matchlist
* `create_blacklist` - Create a matchlist
* `list_blacklists` - List matchlists

### rules_api

* `export_rules` - Bulk export rules
* `list_rules` - List rules
* `read_one_rule` - Get a rule

### sars_api

* `export_sars` - Bulk export sars
* `list_sars` - List sars
* `read_one_sar` - Get a sars

### tag_associations_api

* `list_tags` - List tags

### verification_forms_api

* `create_verification_form` - Verification Forms API

### webhooks_api

* `update_webhook` - Update webhook URL
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
