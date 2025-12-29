import os

def load_payloads(path):
    payloads = []
    if not os.path.exists(path):
        return payloads

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                payloads.append(line)
    return payloads
