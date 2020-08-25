def cache3(func):
    _cache['counter']=0
    def added_value(*args):
        if _cache['counter']==0 or _cache['counter']==3:
            _cache = {'counter': 1}
            value=func(*args)
            return value
        if _cache['counter']==1 or _cache['counter']==2:
            _cache['counter'] = _cache['counter'] + 1
            return value
    return added_value

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
# 1
