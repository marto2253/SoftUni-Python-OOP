def cache(func):
    result = {}

    def wrapper(num):
        if num not in result:
            result[num] = func(num)
        return result[num]

    wrapper.log = result
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(22))
print(fibonacci.log)
