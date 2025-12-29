from bs4 import BeautifulSoup
from core.http_client import fetch
from core.output import ok, info

def run_param_discovery(url):
    info("Mencari parameter")
    r = fetch(url)
    if not r: return

    soup = BeautifulSoup(r.text, "html.parser")
    params = set()

    for i in soup.find_all("input"):
        if i.get("name"):
            params.add(i.get("name"))

    for a in soup.find_all("a"):
        href = a.get("href", "")
        if "?" in href:
            for p in href.split("?")[1].split("&"):
                params.add(p.split("=")[0])

    for p in params:
        ok(f"Parameter ditemukan: {p}")
