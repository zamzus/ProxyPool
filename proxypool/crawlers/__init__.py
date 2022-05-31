import inspect
import pkgutil
from .base import BaseCrawler

crawlers_cls = []

for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    modlue = loader.find_module(name).load_module(name)
    for n, v in inspect.getmembers(modlue):
        if inspect.isclass(v) and issubclass(v, BaseCrawler) and v is not BaseCrawler \
                and not getattr(v, 'ignore', False):
            crawlers_cls.append(v)
