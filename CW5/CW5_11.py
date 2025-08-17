import time


def timer_decorator(func):

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Use perf_counter for precise timing
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds.")
        return result

    return wrapper


@timer_decorator
def example_function():
    """A simple function to demonstrate the timer."""
    time.sleep(1.5)  # Simulate some work
    return "Task completed"


@timer_decorator
def fibonacci_generator(n):
    """A generator function to demonstrate timing with a generator."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# Using the decorated regular function
print(example_function())

# Using the decorated generator function
print("\nGenerating Fibonacci numbers:")
for num in fibonacci_generator(10):
    print(num)
