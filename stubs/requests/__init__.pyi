from .packages import urllib3
from .exceptions import ConnectTimeout, ReadTimeout, ConnectionError

def get(self, url: str = "", proxies=None, verify=True, timeout=None): ...

__all__ = ["get"]
