class SensorDataError(Exception):
    """Base exception for SensorData SDK errors."""
    pass

class ValidationError(SensorDataError):
    """Exception raised for validation errors."""
    pass

class APIError(SensorDataError):
    """Exception raised for API request errors."""
    pass