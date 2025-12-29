import requests
requests.packages.urllib3.disable_warnings()

def fetch(url):
    try:
        return requests.get(url, timeout=10, verify=False)
    except:
        return None
