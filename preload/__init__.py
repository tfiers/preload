from pkg_resources import get_distribution

__version__ = get_distribution(__name__).version

from .preload import preload_with_feedback