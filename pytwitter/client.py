import logging
from pytwitter.rest_adapter import RestAdapter
from pytwitter.exceptions import TwitterAPIException
from pytwitter.models import *


class TwitterClient:
    def __init__(self, bearer: str = '', ver: str = '', verify_ssl: bool = True, logger: logging.Logger = None):
        self._rest_adapter = RestAdapter(bearer, ver, verify_ssl, logger)
