from .deviantart import main as DeviantArtExtractor
from .furaffinity import main as FurAffinityExtractor
from .furrynetwork import main as FurryNetworkExtractor
from .tumblr import main as TumblrExtractor

__all__ = [
    "DeviantArtExtractor",
    "FurAffinityExtractor",
    "FurryNetworkExtractor",
    "TumblrExtractor"
]
