from functools import wraps


def validate_positive(func):
    _MY_ZERO = 0

    @wraps(func)
    def validator(*args, **kwargs):
        for element in list(args) + list(kwargs.values()):
            if (
                not isinstance(element, (int, float))
            ):
                raise TypeError('Все аргументы должны быть числами')
            if element < _MY_ZERO:
                raise ValueError("Все аргументы должны быть положительными")
        return func(*args, **kwargs)

    return validator
