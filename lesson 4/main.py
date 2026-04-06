from time import perf_counter

def timer(arg):
    def inner(func):
        def wrapper(*args):
            start = perf_counter()
            func(*args)
            end = perf_counter()
            print(round(end-start, 2))
        return wrapper
    return inner

@timer("Twoja Stara") # decorator = _timer(count)
def count(value: int, say_hello: bool = False) -> None:
    if say_hello:
        print('Hello!')
    for i in range(value):
        print(i)
        
count(1000, True)