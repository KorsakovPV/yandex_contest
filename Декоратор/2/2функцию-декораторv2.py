def cache3(func):
    count = 0
    def added_value():
        if count==0 or count==3:
            count=1
            value=func()
            return value
        elif count==1 or count==2:
            count = count + 1
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
