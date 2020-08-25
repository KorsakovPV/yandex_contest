def cache_args(func):
    _cache = {'num': 0, 'result': 0}
    def cache_checker(*args):
        if args[0] == _cache['num']:
            return _cache['result']
        else:
            _cache["num"] = args[0]
            _cache['result'] = func(*args)
            return _cache['result']
    return cache_checker

    
@cache_args
def long_heavy(num, *args):
     print(f"Долго и сложно {num}")
     return num**num

print(long_heavy('1',3,4))
# Долго и сложно 1
# 1
print(long_heavy(1,3,4))
# 1
print(long_heavy(2,3,4))
# Долго и сложно 2
# 4
print(long_heavy(2,3,4))
# 4
print(long_heavy(2,3,4))
# 4
