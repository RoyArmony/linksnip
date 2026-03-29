"""
Custom exceptions for linksync SDK
"""


class LinksyncError(Exception):
    """Base exception for all linksync errors"""
    pass


class AuthenticationError(LinksyncError):
    """Raised when API key is invalid or missing"""
    pass


class InvalidURLError(LinksyncError):
    """Raised when provided URL is invalid"""
    pass


class LinkNotFoundError(LinksyncError):
    """Raised when link ID does not exist"""
    pass


class LinkExistsError(LinksyncError):
    """Raised when trying to create a link that already exists"""
    pass


class ValidationError(LinksyncError):
    """Raised when input validation fails"""
    pass


class APIError(LinksyncError):
    """Raised when API returns an error"""
    
    def __init__(self, message, status_code=None, error_code=None):
        super().__init__(message)
        self.status_code = status_code
        self.error_code = error_code


class ConnectionError(LinksyncError):
    """Raised when unable to connect to API"""
    pass
