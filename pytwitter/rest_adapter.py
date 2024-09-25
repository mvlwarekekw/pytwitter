import requests
import urllib3
import logging
from json import JSONDecodeError

from requests import Response

from .errors import TwitterAPIException
from .models import APIResponse


class RestAdapter:
    def __init__(self, bearer: str = "", api_ver: str = '2', verify_ssl: bool = True, logger: logging.Logger = None):
        """
        Constructor for RestAdapter
       :param bearer: Bearer Authentication Token
       :param api_ver: API Version, defaults to 2
       :param verify_ssl: SSL/TLS Certificate validation, can turn off with False
       :param logger: Logger instance, defaults to logger.logger(__name__)
       """
        self.url = f"https://api.twitter.com/{api_ver}"
        self._logger = logger or logging.getLogger(__name__)
        self._bearer = bearer
        self._verify_ssl = verify_ssl
        # Disable SSL/TSL Certificate validation
        if not verify_ssl:
            urllib3.disable_warnings()

    def bearer_auth(self, r):
        """
        Bearer Authorization Method
        :param r: request object
        :return: Updated request object
        """
        r.headers['Authorization'] = f"Bearer {self._bearer}"
        r.headers['User-Agent'] = 'Pytwitter v1.0'

        return r

    def _request(self, method: str, endpoint: str, params: dict = None, data: dict = None) -> APIResponse | None:
        """
        Request method for Twitter API
        :param method: HTTP method
        :param endpoint: API endpoint
        :param params: HTTP Parameters
        :param data: Data to be sent, only needed on POST, PUT, DELETE

        :return APIResponse: Returns API Response object
        """
        url = f"{self.url}{endpoint}"

        status_code = 400
        pre_log_line = f"API Request: method={method}, url={url}, params={params}"
        post_log_line = ', '.join((pre_log_line, "success={}, status_code={}, message={}"))

        # API Request, catch exceptions
        try:
            self._logger.debug(msg=pre_log_line)
            response: Response = requests.request(method=method, url=url, verify=self._verify_ssl, auth=self.bearer_auth, params=params, data=data)
            status_code = response.status_code
        except requests.exceptions.RequestException as e:
            self._logger.error(msg=str(e))
            raise TwitterAPIException(f"Request failed with code {status_code}. Error occured while making request.")
        except Exception as e:
            self._logger.error(msg=str(e))
            raise TwitterAPIException(f"Request failed with code {status_code}. Unknownw error occured while making request")

        # Deserialize JSON response or raise error if request failed
        try:
            out_data = response.json()
        except (ValueError, JSONDecodeError, KeyError) as e:
            self._logger.error(msg=post_log_line.format(False, status_code, response.reason))
            raise TwitterAPIException("Bad JSON response.") from e

        # Checked if the request returned a successful status code
        is_success = 200 <= status_code <= 299
        log_line = post_log_line.format(is_success, status_code, response.reason)

        if is_success:
            self._logger.debug(msg=log_line)
            return APIResponse(status_code, response.reason, out_data)
        elif status_code == 429:
            raise TwitterAPIException(f"Too many requests.")
        self._logger.error(msg=log_line)
        raise TwitterAPIException(f"Request failed with code {status_code}. {response.json()}")

    def get(self, endpoint: str, params: dict = None) -> APIResponse:
        """
        :param endpoint: API Endpoint
        :param params: Parameters e.g. {'usernames': 'mvlwarekekw'}
        :return: JSON-Object
        :raise: RequestException if status code not 2xx
        """

        return self._request("GET", endpoint, params)

    def post(self, endpoint: str, params: dict = None, data: dict = None) -> APIResponse:
        """
        :param endpoint: API Endpoint
        :param params: Parameters e.g. {'usernames': 'mvlwarekekw'}
        :param data: Data to be posted
        :return: JSON-Object
        :raise: RequestException if status code not 2xx
        """

        return self._request("POST", endpoint, params, data)

    def delete(self, endpoint: str, params: dict = None, data: dict = None) -> APIResponse:
        """
        :param endpoint: API Endpoint
        :param params: Parameters e.g. {'usernames': 'mvlwarekekw'}
        :param data: Data to be deleted
        :return: JSON-Object
        :raise: RequestException if status code not 2xx
        """

        return self._request("DELETE", endpoint, params, data)

    def put(self, endpoint: str, params: dict = None, data: dict = None) -> APIResponse:
        """
        :param endpoint: API Endpoint
        :param params: Parameters e.g. {'usernames': 'mvlwarekekw'}
        :param data: Data to be put
        :return: JSON-Object
        :raise: RequestException if status code not 2xx
        """

        return self._request("PUT", endpoint, params, data)

