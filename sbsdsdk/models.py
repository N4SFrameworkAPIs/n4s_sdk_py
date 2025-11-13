from dataclasses import dataclass
from typing import Any, Dict
from urllib.parse import urlparse


@dataclass
class SbsdskPayload:
    user_agent: str
    targetURL: str
    v_url: str
    bm_so: str
    language: str
    script: Any          # can be str, dict, list, etc.

    def validate(self) -> None:
        """Validate all required fields and URL format."""
        if not self.user_agent:
            raise ValueError("user_agent is required")
        if not self.is_valid_url(self.targetURL):
            raise ValueError("targetURL must be a valid URL")
        if not self.is_valid_url(self.v_url):
            raise ValueError("v_url must be a valid URL")
        if not self.bm_so:
            raise ValueError("bm_so is required")
        if not self.language:
            raise ValueError("language is required")
        if self.script is None:
            raise ValueError("script is required")

    @staticmethod
    def is_valid_url(url: str) -> bool:
        """Check that the URL contains scheme and netloc."""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except Exception:
            return False

    def to_dict(self) -> Dict[str, Any]:
        """Convert the payload to a dictionary for JSON serialization."""
        return {
            "user_agent": self.user_agent,
            "targetURL": self.targetURL,
            "v_url": self.v_url,
            "bm_so": self.bm_so,
            "language": self.language,
            "script": self.script,
        }