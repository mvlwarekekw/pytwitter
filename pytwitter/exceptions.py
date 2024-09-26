

class TwitterAPIException(Exception):
    """
    Exception when request does not return a status code 2xx
    """
    def __init__(self, message: str = ""):
        super().__init__(f"{message}")

