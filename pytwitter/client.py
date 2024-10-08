import logging
from pytwitter.rest_adapter import RestAdapter
from pytwitter.exceptions import TwitterAPIException
from pytwitter.models import *


class TwitterClient:
    def __init__(self, bearer: str = '', ver: str = '', verify_ssl: bool = True, logger: logging.Logger = None):
        self._rest_adapter = RestAdapter(bearer, ver, verify_ssl, logger)

    def find_user_by_name(self, name: str):
        result = self._rest_adapter.get(
            endpoint=f"/users/by/username/{name}"
        )
        user = User(**result.data["data"])

        return user

    def find_users_by_names(self, names: [str]):
        result = self._rest_adapter.get(
            endpoint=f"/users/by",
            params={
                'usernames': names
            }
        )

        user = User(**result.data["data"])

        return user

    def find_user_by_id(self):
        result = self._rest_adapter.get(endpoint=f"/users/{id}")
        user = User(**result.data["data"])

        return user

    def find_users_by_ids(self, ids: [str]):
        result = self._rest_adapter.get(
            endpoint=f"/users",
            params={
                'usernames': ids
            }
        )

        user = User(**result.data["data"])

        return user

    def followers_by_user_id(self, user_id: int):
        result = self._rest_adapter.get(
            endpoint=f"/users/{user_id}/followers"
        )

        followers = [User(**follower) for follower in result.data]

        return followers

    def following_by_user_id(self, user_id: int):
        result = self._rest_adapter.get(
            endpoint=f"/users/{user_id}/following"
        )

        following = [User(**following) for following in result.data]

        return following

    def list_by_id(self, list_id: int):
        result = self._rest_adapter.get(
            endpoint=f"/lists/{list_id}"
        )

        return result

    def user_owned_lists(self, user_id: int):
        result = self._rest_adapter.get(
            endpoint=f"/users/{user_id}/owned_lists"
        )

        return result

    def list_tweet_lookup(self, list_id: int):
        result = self._rest_adapter.get(
            endpoint=f"/lists/{list_id}/tweets"
        )

        tweets = [Tweet(**tweet) for tweet in result.data]

        return tweets


