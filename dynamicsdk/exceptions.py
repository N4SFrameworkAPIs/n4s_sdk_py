class DynamicError(Exception):
    """Base exception for Dynamic SDK errors."""
    pass

class ValidationError(DynamicError):
    """Exception raised for validation errors."""
    pass

class APIError(DynamicError):
    """Exception raised for API request errors."""
    pass
