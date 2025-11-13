class SbsdskError(Exception):
    """Base exception for SbsdskClient errors."""
    pass


class SbsdskConnectionError(SbsdskError):
    """Raised for network or connection errors."""
    pass


class SbsdskAPIError(SbsdskError):
    """Raised for API-level errors (4xx/5xx)."""
    pass