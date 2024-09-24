import requests
import urllib3

from errors import RequestException

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

    def _request(self, method: str, endpoint: str, params: dict = None, data: dict = None):
        url = f"{self.url}{endpoint}"

        response = requests.request(method=method, url=url, verify=self._verify_ssl, auth=self.bearer_auth, params=params, data=data)

        if 200 <= response.status_code <= 299:
            return response.json()
        raise RequestException(response.status_code)

    def get(self, endpoint: str, params: dict = None):
        """
        :param endpoint: api endpoint to fetch, e.g. 'users/by'
        :param params: parametres for api endpoint e.g. {'usernames': 'mvlwarekekw'}
        :return: JSON-Object
        :raise: RequestException if status code not 2xx
        """

        return self._request("GET", endpoint, params)

    def post(self, endpoint: str, params: dict = None, data: dict = None):
        """
        :param endpoint: api endpoint to fetch, e.g. 'users/by'
        :param params: parametres for api endpoint e.g. {'usernames': 'mvlwarekekw'}
        :param data: data to be posted to the API
        :return: JSON-Object
        :raise: RequestException if status code not 2xx
        """

        return self._request("POST", endpoint, params, data)

    def delete(self, endpoint: str, params: dict = None, data: dict = None):
        """
        :param endpoint: api endpoint to fetch, e.g. 'users/by'
        :param params: parametres for api endpoint e.g. {'usernames': 'mvlwarekekw'}
        :param data: data to be posted to the API
        :return: JSON-Object
        :raise: RequestException if status code not 2xx
        """

        return self._request("DELETE", endpoint, params, data)

    def put(self, endpoint: str, params: dict = None, data: dict = None):
        """
        :param endpoint: api endpoint to fetch, e.g. 'users/by'
        :param params: parametres for api endpoint e.g. {'usernames': 'mvlwarekekw'}
        :param data: data to be posted to the API
        :return: JSON-Object
        :raise: RequestException if status code not 2xx
        """

        return self._request("PUT", endpoint, params, data)

