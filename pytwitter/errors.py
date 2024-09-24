

class RequestException(Exception):
    """
    Exception when request does not return a status code 2xx
    """
    def __init__(self, status_code, message: str = ""):
        super().__init__(f"Request failed with code {status_code}. {message}")


