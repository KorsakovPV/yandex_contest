def cache3(func):
    _cache = {'count': 0}
    def func_with_cache():
        
        if _cache['count'] < 3:
            
            if 'func_result' not in _cache:
                _cache['count'] += 1
                _cache['func_result'] = func()
            else:
                _cache['count'] += 1
        else:
            
            _cache['count'] = 0
            _cache['func_result'] = func()
            
        return _cache['func_result']
    return func_with_cache
    
@cache3
def heavy():
    print('Сложные вычисления')
    return 1

print(heavy())
# Сложные вычисления
# 1
print(heavy())
# 1
print(heavy())
# 1
# Опять кеш устарел, надо вычислять заново
print(heavy())
# Сложные вычисления
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())