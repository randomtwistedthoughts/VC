from vulnclaw.tools.http import fetch_url
from vulnclaw.tools.registry import ToolRegistry
from vulnclaw.evidence.models import Evidence
from vulnclaw.evidence.store import EvidenceStore


registry = ToolRegistry()
registry.register("fetch_url", fetch_url)

evidence_store = EvidenceStore()

url = "https://example.com"

result = registry.execute(
    "fetch_url",
    url=url,
)

evidence = Evidence(
    tool="fetch_url",
    target=url,
    data=result,
)

evidence_store.add(evidence)

print("Tools:", registry.list_tools())
print("Status:", result.get("status_code"))
print("Success:", result.get("success"))
print("Evidence:", evidence_store.count())
