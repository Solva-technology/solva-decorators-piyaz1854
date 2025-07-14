from functools import wraps


def validate_positive(func):

    @wraps(func)
    def validator(*args, **kwargs):
        for element in list(args) + list(kwargs.values()):
            if (
                isinstance(element, (int, float))
                and element <= 0
            ):
                raise ValueError('Все аргументы должны быть положительными')
        return func(*args, **kwargs)

    return validator
