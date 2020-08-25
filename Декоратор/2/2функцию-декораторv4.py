def cache3(func):
    _cache = {'count': 0, 'result': None}

    def run():
        if 1 <= _cache['count'] < 3:
            _cache['count'] += 1
            return _cache['result']
        else:
            _cache['count'] = 1
            _cache['result'] = func()
            return _cache['result']

    return run


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