def new_decorator(original_decorator):
    def wrap_func():
        print('Here goes some extra code before the original function')
        original_decorator()
        print('Here goes the second part of the code after launching the original function')
    return wrap_func
@new_decorator
def func_ready_to_get_passed():
    print('I want to be decorated')
    