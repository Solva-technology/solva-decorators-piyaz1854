from collections import OrderedDict
from functools import wraps


def simple_cache(func):
    _MAX_CACHE_SIZE = 10
    cache = OrderedDict()

    @wraps(func)
    def cacher(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        try:
            hash(key)
        except TypeError:
            raise TypeError('Невозможно захэшировать переданные данные.')
        if key in cache:
            print("Из кэша")
            return cache[key]
        result = func(*args, **kwargs)
        if len(cache) >= _MAX_CACHE_SIZE:
            cache.popitem(last=False)
        cache[key] = result
        return result

    return cacher
