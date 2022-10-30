import functools as f


numbers = [1, 2, 3, 4, 5]
result = f.reduce(lambda a, b: a + b, numbers)
print(result)

