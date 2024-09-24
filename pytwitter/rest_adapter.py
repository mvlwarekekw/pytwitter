import requests
import urllib3
from json import JSONDecodeError

from requests import Response

from .errors import TwitterAPIException
from .models import APIResponse


class RestAdapter:
    def __init__(self, bearer: str = "", api_ver: str = 'v1', verify_ssl: bool = True):
        self.url = f"https://api.twitter.com/{api_ver}"
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

        try:
            response: Response = requests.request(method=method, url=url, verify=self._verify_ssl, auth=self.bearer_auth, params=params, data=data)
            status_code = response.status_code
        except requests.exceptions.RequestException as e:
            raise TwitterAPIException(f"Request failed with code {status_code}. Error occured while making request.")
        except Exception as e:
            raise TwitterAPIException(f"Request failed with code {status_code}. Unknownw error occured while making request")

        try:
            out_data = response.json()
        except (ValueError, JSONDecodeError, KeyError) as e:
            raise TwitterAPIException("Bad JSON response.") from e

        if 200 <= status_code <= 299:
            return APIResponse(status_code, response.reason, out_data)
        elif status_code == 429:
            raise TwitterAPIException(f"Too many requests.")
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

