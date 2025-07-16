from collections import defaultdict
import time

_rate_store = defaultdict(list)

def is_rate_limited(client_id: str, limit: int = 10, window: int = 60) -> bool:
    now = time.time()
    requests = [ts for ts in _rate_store[client_id] if now - ts < window]
    _rate_store[client_id] = requests

    if len(requests) >= limit:
        return True

    _rate_store[client_id].append(now)
    return False
