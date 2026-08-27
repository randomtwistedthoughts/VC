import httpx

def fetch_url(url: str) -> dict:
  try:
    response = httpx.get(url, timeout=10.0)
    
    return {
      "success": True,
      "url": str(response.url),
      "status_code": response.status_code,
      "headers": dict(response.headers),
      "body": response.text,
    }
  except Exception as exc:
    return {
      "success": False,
      "url": url,
      "error": str(exc).
    }
    
