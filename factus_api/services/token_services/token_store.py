"""Store and manage API tokens."""

import time


class TokenManager:
    """Handle token storage and expiration time."""

    def __init__(self) -> None:
        """Initialize an empty token store."""
        self.tokens: dict = {}

    def token_storage(self, token, expires_at) -> None:
        """Save the token and calculate its expiration time."""
        self.tokens = token
        self.tokens["expires_at"] = expires_at + time.time()


tokens = TokenManager()
