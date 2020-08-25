def cache3(func):
    cache = {'res': func(), 'counter': 0}

    def save_three_times():
        if cache['counter'] == 3:
            cache['counter'] = 0
            cache['res'] = func()
            return cache['res']
        cache['counter'] += 1
        return cache['res']
    return save_three_times


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
