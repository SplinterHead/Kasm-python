from .users import get_users


class Kasm:
    base_url: str
    authorisation_json: dict

    def __init__(
        self,
        url: str,
        api_key: str,
        api_key_secret: str,
    ):
        # Ensure the http protocol is prefixed to the URL
        self.base_url = url if "://" in url else f"https://{url}"
        self.authorisation_json = {"api_key": api_key, "api_key_secret": api_key_secret}

    ################
    # Users
    ################
    def get_users(self):
        return get_users(self.base_url, self.authorisation_json)
