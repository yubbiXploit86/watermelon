from core.http_client import fetch
from core.output import ok, warn

def run_wp_scan(url):
    r = fetch(url + "/wp-json/")
    if r and r.status_code == 200:
        ok("WordPress REST API aktif")

    r2 = fetch(url + "/xmlrpc.php")
    if r2 and r2.status_code == 200:
        warn("XML-RPC aktif")
