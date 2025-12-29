from core.http_client import fetch
from core.output import warn, ok

def run_header_scan(url):
    r = fetch(url)
    if not r: return

    headers = r.headers
    if "X-Frame-Options" not in headers:
        warn("X-Frame-Options tidak ada")
    else:
        ok("X-Frame-Options aktif")
