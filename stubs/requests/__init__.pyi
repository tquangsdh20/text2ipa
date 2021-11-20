from .packages import urllib3
from .exceptions import ConnectTimeout, ReadTimeout, ConnectionError

def get(self, url: str = "", proxies=None, verify=True, timeout=None): ...

def post(self, url: str = "", proxies=None, data=None , timeout=None, verify=True): ...

__all__ = ["get","post"]
