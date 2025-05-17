#decorators are func that modify or enchance the behaviour of the other functions without changing their code
def decorator_function(original_function):
    def wrapper():
        print("before function")
        original_function()
        print("after the function")
        