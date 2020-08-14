def check(x):
    global count_3
    global count_5
    if x % 3 == 0 and x % 5 == 0:
        count_3 = count_3 + 1
        count_5 = count_5 + 1
        return 'foobar'
    elif x % 3 == 0:
        count_3 = count_3 + 1
        return 'foo'
    elif x % 5 == 0:
        count_5 = count_5 + 1
        return 'bar'
    else:
        return x


array = []
i = 1
count_3 = 0
count_5 = 0
while i < 101:
    array.append(check(i))
    i = i + 1
print(array)
print("Количество чисел, кратных 3:", count_3)
print("Количество чисел, кратных 5:", count_5)
print("Количество чисел, кратных 3 и 5:", array.count('foobar'))
