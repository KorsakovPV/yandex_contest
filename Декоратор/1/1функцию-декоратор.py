def cache_args(func):
    _cache = {}
    def cache_checker(*args):
        if args[0] in _cache.keys():
            return _cache[args[0]]
        else:
            _cache[args[0]] = func(*args)
            return _cache[args[0]]
    return cache_checker

@cache_args
def long_heavy(num):
     print(f"Долго и сложно {num}")
     return num**num


print(long_heavy(1))
# Долго и сложно 1
# 1
print(long_heavy(1))
# 1
print(long_heavy(2))
# Долго и сложно 2
# 4
print(long_heavy(2))
# 4
print(long_heavy(2))
# 4
print(long_heavy(6))
print(long_heavy(6))
print(long_heavy(6))
