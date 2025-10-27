from dataclasses import dataclass
from typing import Dict, Any
from urllib.parse import urlparse

@dataclass
class Reese84Payload:
    user_agent: str
    url: str
    site: str
    data: str

    def validate(self) -> None:
        """Validate all mandatory fields."""
        if not self.user_agent:
            raise ValueError("user_agent is required")
        if not self.is_valid_url(self.url):
            raise ValueError("url must be a valid URL")
        # if not self.is_valid_url(self.site):
        #     raise ValueError("site must be a valid URL")
        if not self.data:
            raise ValueError("data is required")

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
            "user_agent": self.user_agent,
            "url": self.url,
            #"site": self.site,
            "data": self.data
        }