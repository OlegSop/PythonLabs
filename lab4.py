def wraps(func):
    def wraps_dec(wraps_func):
        def wrapper(*args):
            wrapper.__name__ = func.__name__
            wrapper.__doc__ = func.__doc__
            return wraps_func(*args)
        return wrapper
    return wraps_dec

def decorator(func):
    @wraps(func)
    def wrap_function(*args):
        '''Bring to square number'''
        return func(*args)**2
    return wrap_function

@decorator
def sum_func(num1,num2):
    '''Function that sum two numbers'''
    return num1+num2


if __name__ == '__main__':
    print(sum_func(5,5))
    print(sum_func.__name__)
    print(sum_func.__doc__)

