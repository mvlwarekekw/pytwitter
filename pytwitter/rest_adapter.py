import requests
import urllib3
import logging
from json import JSONDecodeError

from requests import Response

from .errors import TwitterAPIException
from .models import APIResponse


class RestAdapter:
    def __init__(self, bearer: str = "", api_ver: str = 'v1', verify_ssl: bool = True, logger: logging.Logger = None):
        self.url = f"https://api.twitter.com/{api_ver}"
        self._logger = logger or logging.getLogger(__name__)
        self._bearer = bearer
        self._verify_ssl = verify_ssl
        if not verify_ssl:
            urllib3.disable_warnings()

    def bearer_auth(self, r):
        """
        Bearer Authorization Method
        :param r: request object
        :return:
        """
        r.headers['Authorization'] = f"Bearer {self._bearer}"
        r.headers['User-Agent'] = 'Pytwitter v1.0'

        return r

    def _request(self, method: str, endpoint: str, params: dict = None, data: dict = None) -> APIResponse | None:
        url = f"{self.url}{endpoint}"

        status_code = 400
        pre_log_line = f"API Request: method={method}, url={url}, params={params}"
        post_log_line = ', '.join((pre_log_line, "success={}, status_code={}, message={}"))

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

        try:
            out_data = response.json()
        except (ValueError, JSONDecodeError, KeyError) as e:
            self._logger.error(msg=post_log_line.format(False, status_code, response.reason))
            raise TwitterAPIException("Bad JSON response.") from e

        is_success = 200 <= status_code <= 299
        log_line = post_log_line.format(is_success, status_code, response.reason)

        if is_success:
            self._logger.debug(msg=log_line)
            return APIResponse(status_code, response.reason, out_data)
        elif status_code == 429:
            raise TwitterAPIException(f"Too many requests.")
        self._logger.error(msg=log_line)
        raise TwitterAPIException(f"Request failed with code {status_code}.")

    def get(self, endpoint: str, params: dict = None) -> APIResponse:
        """
        :param endpoint: api endpoint to fetch, e.g. 'users/by'
        :param params: parametres for api endpoint e.g. {'usernames': 'mvlwarekekw'}
        :return: JSON-Object
        :raise: RequestException if status code not 2xx
        """

        return self._request("GET", endpoint, params)

    def post(self, endpoint: str, params: dict = None, data: dict = None) -> APIResponse:
        """
        :param endpoint: api endpoint to fetch, e.g. 'users/by'
        :param params: parametres for api endpoint e.g. {'usernames': 'mvlwarekekw'}
        :param data: data to be posted to the API
        :return: JSON-Object
        :raise: RequestException if status code not 2xx
        """

        return self._request("POST", endpoint, params, data)

    def delete(self, endpoint: str, params: dict = None, data: dict = None) -> APIResponse:
        """
        :param endpoint: api endpoint to fetch, e.g. 'users/by'
        :param params: parametres for api endpoint e.g. {'usernames': 'mvlwarekekw'}
        :param data: data to be posted to the API
        :return: JSON-Object
        :raise: RequestException if status code not 2xx
        """

        return self._request("DELETE", endpoint, params, data)

    def put(self, endpoint: str, params: dict = None, data: dict = None) -> APIResponse:
        """
        :param endpoint: api endpoint to fetch, e.g. 'users/by'
        :param params: parametres for api endpoint e.g. {'usernames': 'mvlwarekekw'}
        :param data: data to be posted to the API
        :return: JSON-Object
        :raise: RequestException if status code not 2xx
        """

        return self._request("PUT", endpoint, params, data)

