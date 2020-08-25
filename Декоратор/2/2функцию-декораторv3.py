def cache3(func):
        _cache = {'counter': 0}
        def added_value():
            if _cache['counter'] == 0:
                _cache['counter'] = _cache['counter'] + 1
                _cache['value'] = func()
                #print('0000')
                return _cache['value']
            elif _cache['counter'] in [1, 2]:
                _cache['counter'] = _cache['counter'] + 1
                #print('0102')
                return _cache['value']
            elif _cache['counter'] == 3:
                print('')
                print('Опять кеш устарел, надо вычислять заново')
                _cache['counter'] = 1
                _cache['value'] = func()
                #print('0003')
                return _cache['value']
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
print(heavy())
