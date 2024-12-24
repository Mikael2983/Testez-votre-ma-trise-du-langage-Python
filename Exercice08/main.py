def log_decorator(func):
    def wrapper():
        print("voici le message avant la fonction")
        func()
        print("voici le message après la fonction")
    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()
