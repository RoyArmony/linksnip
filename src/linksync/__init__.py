"""linksync - Python SDK for creating and managing short URLs.

A generic URL shortening client that works with any compatible backend API.
"""

__version__ = "0.2.1"

from .client import Client
from .exceptions import (
    LinksyncError,
    AuthenticationError,
    InvalidURLError,
    LinkNotFoundError,
    LinkExistsError,
    ValidationError,
    APIError,
    ConnectionError
)

__all__ = [
    "Client",
    "LinksyncError",
    "AuthenticationError",
    "InvalidURLError",
    "LinkNotFoundError",
    "LinkExistsError",
    "ValidationError",
    "APIError",
    "ConnectionError",
]
