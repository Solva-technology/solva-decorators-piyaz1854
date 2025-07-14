from functools import wraps


def log(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        positional = [repr(a) for a in args]
        named = [f'{k}={repr(v)}' for k, v in kwargs.items()]
        args_str = ', '.join(positional + named)
        print(f'Вызов: {func.__name__}({args_str})')
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result

    return wrapper
