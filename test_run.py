from vulnclaw.tools.http import fetch_url
from vulnclaw.tools.registry import ToolRegistry


registry = ToolRegistry()

registry.register("fetch_url", fetch_url)

print("Tools:", registry.list_tools())

result = registry.execute(
    "fetch_url",
    url="https://example.com",
)

print("Status:", result.get("status_code"))
print("Success:", result.get("success"))
