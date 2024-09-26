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


class Tweet:
    def __init__(
            self,
            id: str,
            text: str,
            edit_history_tweets: dict,
            attachments: dict,
            author_id: str,
            context_annotations: list,
            conversation_id: str,
            created_at: str,
            edit_controls: dict,
            entities: dict,
            in_reply_to_user: str,
            lang: str,
            non_public_metrics: dict,
            organic_metrics: dict,
            possibly_sensitive: bool,
            promoted_metrics: dict,
            public_metrics: dict,
            referenced_tweets: list,
            reply_settings: str,
            withheld: dict
    ):
        self.id = id
        self.text = text
        self.edit_history_tweets = edit_history_tweets
        self.attachments = attachments
        self.author_id = author_id
        self.context_annotations = context_annotations
        self.conversation_id = conversation_id
        self.created_at = created_at
        self.edit_controls = edit_controls
        self.entities = entities
        self.in_reply_to_user = in_reply_to_user
        self.lang = lang
        self.non_public_metrics = non_public_metrics
        self.organic_metrics = organic_metrics
        self.possibly_sensitive = possibly_sensitive
        self.promoted_metrics = promoted_metrics
        self.public_metrics = public_metrics
        self.referenced_tweets = referenced_tweets
        self.reply_settings = reply_settings
        self.withheld = withheld


class Media:
    def __init__(
            self,
            media_key: str,
            type: str,
            url: str,
            duration_ms: int,
            height: int,
            non_public_metrics: dict,
            organic_metrics: dict,
            preview_image_url: str,
            promoted_metrics: dict,
            public_metrics: dict,
            width: int,
            alt_text: str,
            variants: dict
    ):
        self.media_key = media_key
        self.type = type
        self.url = url
        self.duration_ms = duration_ms
        self.height = height
        self.non_public_metrics = non_public_metrics
        self.organic_metrics = organic_metrics
        self.preview_image_url = preview_image_url
        self.promoted_metrics = promoted_metrics
        self.public_metrics = public_metrics
        self.width = width
        self.alt_text = alt_text
        self.variants = variants


class Poll:
    def __init__(
            self,
            id: str,
            options: dict,
            duration_minutes: int,
            end_datetime: str,
            voting_status: str
    ):
        self.id = id
        self.options = options
        self.duration = duration_minutes
        self.end_datetime = end_datetime
        self.voting_status = voting_status


class Place:
    def __init__(
            self,
            full_name: str,
            id: str,
            contained_within: dict,
            country: str,
            country_code: str,
            geo: dict,
            name: str,
            place_type: str
    ):
        self.full_name = full_name
        self.id = id
        self.contained_within = contained_within
        self.country = country
        self.country_code = country_code
        self.geo = geo
        self.name = name
        self.place_type = place_type
