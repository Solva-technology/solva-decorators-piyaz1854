from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        positional = [repr(a) for a in args]
        named = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        args_str = ", ".join(positional + named)
        print(f"Вызов: {func.__name__}({args_str})")
        try:
            result = func(*args, **kwargs)
            print(f"Результат: {result}")
            return result
        except Exception as e:
            print(f'Исключение: {e}')
            raise

    return wrapper
