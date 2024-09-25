import array


class APIResponse:
    def __init__(self, status_code: int, message: str = '', data: [{}] = None):
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else {}


class User:
    def __init__(
            self,
            id: str,
            name: str,
            username: str,
            connection_status: list = [],
            created_at: str = '',
            description: str = '',
            entities: dict = {},
            location: str = '',
            pinned_tweet_id: str = '',
            profile_image_url: str = '',
            protected: str = '',
            public_metrics: dict = {},
            url: str = '',
            verified: bool = False
    ):
        self.id = id
        self.name = name
        self.username = username
        self.connection_status = connection_status
        self.created_at = created_at
        self.description = description
        self.entities = entities
        self.location = location
        self.pinned_tweet_id = pinned_tweet_id
        self.profile_image_url = profile_image_url
        self.protected = protected
        self.public_metrics = public_metrics
        self.url = url
        self.verified = verified


