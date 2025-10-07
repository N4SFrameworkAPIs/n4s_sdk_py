from dataclasses import dataclass
from typing import Dict, Any
from urllib.parse import urlparse

@dataclass
class SensorData:
    targetURL: str
    user_agent: str
    abck: str
    bm_sz: str
    dynamic: Dict[str, Any]
    req_number: int

    def validate(self) -> None:
        """Validate all mandatory fields."""
        if not self.targetURL:
            raise ValueError("targetURL is required")
        if not self.is_valid_url(self.targetURL):
            raise ValueError("targetURL must be a valid URL")
        if not self.user_agent:
            raise ValueError("user_agent is required")
        if not self.abck:
            raise ValueError("abck is required")
        if not self.bm_sz:
            raise ValueError("bm_sz is required")
        if not isinstance(self.dynamic, dict):
            raise ValueError("dynamic must be a dictionary")
        if not all(k in self.dynamic for k in ['ver', 'key', 'dvc', 'din']):
            raise ValueError("dynamic must contain ver, key, dvc, and din")
        if not isinstance(self.req_number, int) or self.req_number < 0 or self.req_number > 6:
            raise ValueError("req_number must be an integer between 0 and 6")

    @staticmethod
    def is_valid_url(url: str) -> bool:
        """Validate URL format."""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "targetURL": self.targetURL,
            "user_agent": self.user_agent,
            "abck": self.abck,
            "bm_sz": self.bm_sz,
            "dynamic": self.dynamic,
            "req_number": self.req_number
        }
