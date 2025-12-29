from core.http_client import fetch
from core.utils import load_payloads
from core.output import warn, bad, info

def run_sqli_scan(url):
    info("Analisis SQL Injection")
    payloads = load_payloads("payloads/sqli.txt")

    base = fetch(url)
    if not base: return

    hits = 0
    for p in payloads:
        r = fetch(f"{url}?id={p}")
        if r and len(r.text) != len(base.text):
            hits += 1
            warn("Perubahan respon terdeteksi")

    if hits >= 2:
        bad("Indikasi SQL Injection kuat")
