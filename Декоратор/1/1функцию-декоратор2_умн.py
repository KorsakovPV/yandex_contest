def cache_args(func):
    _cache = {}

    def cache_checker(*args):
        if args in _cache.keys():
            return _cache[args]
        else:
            _cache[args] = func(*args)
            return _cache[args]

    return cache_checker


@cache_args
def long_heavy(*args):
    if args == ():
        sum = 'None'
    elif len(args) == 1:
        sum = args[0]
    else:
        sum = 1
        for i in args:
            sum = sum * i
    print(f"Долго и сложно {sum}")
    return sum


print(long_heavy())
# Долго и сложно 0
# 0
print(long_heavy())
# 0
print(long_heavy(1))
# Долго и сложно 1
# 1
print(long_heavy(1))
# 1
print(long_heavy(2, 3))
# Долго и сложно 6
# 6
print(long_heavy(2, 3))
# 6
print(long_heavy(2, 3, 4))
# Долго и сложно 24
# 24
print(long_heavy(2, 3, 4))
# 24
print(long_heavy(2, 3, 4, 5))
# Долго и сложно 120
# 120
print(long_heavy(2, 3, 4, 5))
# 120
