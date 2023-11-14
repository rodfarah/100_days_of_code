inputs = eval(input())


def logging_decorator(my_func):
    def wrapper(*args):
        result = my_func(*args)
        print(f"You called {my_func.__name__}{args}\nIt returned {result}")
    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a*b*c


print(a_function(inputs[0], inputs[1], inputs[2]))
