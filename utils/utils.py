import functools


class DecoratorClass:
    @staticmethod
    def status_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            stars = "*" * 50
            try:
                print(stars)
                print(f"Starting the function '{func.__name__}'...")
                result = func(*args, **kwargs)
                print(f"Function '{func.__name__}' has been successfully completed.")
                print(stars)
                return result
            except Exception as e:
                print(stars)
                print(f"An error occurred in function '{func.__name__}': {e}")
                print(stars)
                # Optionally, re-raise the exception if you want the program to halt or for further handling
                # raise

        return wrapper



