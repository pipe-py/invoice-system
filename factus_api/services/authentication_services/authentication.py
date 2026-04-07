"""Manage authentication"""

from config.settings import env
from ...client.http_client import requests_http
from ..token_services.token_store import tokens
from ...utils.constants import ENDPOINTS


class Authentication:
    """Store API credentials from environment variables."""

    username = env("USER_NAME")
    password = env("PASSWORD")
    client_id = env("CLIENT_ID")
    client_secret = env("CLIENT_SECRET")

    def auth_payload(self):
        """Build and return the payload for the authentication request"""
        return {
            "grant_type": "password",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "username": self.username,
            "password": self.password,
        }

    def auth_header(self):
        """Return header for the authentication request"""
        return {"Accept": "application/json"}

    def api_auth(self):
        """Send request to get a new token and save it."""
        endpoint = ENDPOINTS["authentication"]

        response = requests_http(
            method="POST",
            url=endpoint,
            data=self.auth_payload(),
            header=self.auth_header(),
        )
        tokens.token_storage(token=response, expires_at=response["expires_in"])
