import os


class ExotelProvider:

    def __init__(self):
        self.api_key = os.getenv("EXOTEL_API_KEY")
        self.api_token = os.getenv("EXOTEL_API_TOKEN")
        self.account_sid = os.getenv("EXOTEL_ACCOUNT_SID")
        self.subdomain = os.getenv(
            "EXOTEL_SUBDOMAIN",
            "api.in.exotel.com"
        )

    def is_configured(self):
        return all([
            self.api_key,
            self.api_token,
            self.account_sid
        ])

    def get_call_connect_url(self):
        return (
            f"https://{self.api_key}:{self.api_token}"
            f"@{self.subdomain}"
            f"/v1/Accounts/{self.account_sid}/Calls/connect"
        )