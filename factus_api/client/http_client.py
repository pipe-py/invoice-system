"""Helper to work with HTTP requests"""

import requests
from typing import Literal


def requests_http(
    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"],
    url: str,
    params: dict | None = None,
    data: dict | None = None,
    header: dict | None = None,
    timeout: int = 5,
) -> dict | int:
    """
    Send an HTTP request and return the response.

    Args:
        method (Literal["GET", "POST", "PUT", "PATCH", "DELETE"]): HTTP method name.
        url (str): Endpoint URL.
        params (dict | None): Optional query parameters.
        data (dict | None): Optional requests body as a dictionary.
        header (dict | None): Optional HTTP header.
        timeout (int): Request timeout in seconds (default 5).

    Returns:
        dict | int: JSON response if status code is 200, otherwise the HTTP status code.

    """
    response = requests.request(
        method=method,
        url=url,
        params=params,
        data=data,
        headers=header,
        timeout=timeout,
    )

    if response.status_code == 200:
        return response.json()
    return response.status_code
