from functools import wraps


def simple_cache(func):
    cache = {}

    @wraps(func)
    def cacher(*args, **kwargs):
        hash = args + tuple(sorted(kwargs.items()))
        if hash in cache:
            print("Из кэша")
            return cache[hash]
        result = func(*args, **kwargs)
        cache[hash] = result
        return result

    return cacher
