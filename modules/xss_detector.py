from core.utils import load_payloads
from core.http_client import fetch
from core.output import warn, info

def run_xss_scan(url):
    info("Analisis XSS")
    payloads = load_payloads("payloads/xss.txt")

    for p in payloads:
        r = fetch(f"{url}?q={p}")
        if r and p in r.text:
            warn("Refleksi input terdeteksi")
