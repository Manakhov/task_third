def check(x):
    if x % 3 == 0 and x % 5 == 0:
        return 'foobar'
    elif x % 3 == 0:
        return 'foo'
    elif x % 5 == 0:
        return 'bar'
    else:
        return x


def count(checked_array, key):
    counter = 0
    for value in checked_array:
        if value == 'foobar':
            counter = counter + 1
        elif value == 'foo' and key == 3:
            counter = counter + 1
        elif value == 'bar' and key == 5:
            counter = counter + 1
    return counter


array = []
i = 1
while i < 101:
    array.append(check(i))
    i = i + 1
print(array)
print("Количество чисел, кратных 3:", count(array, 3))
print("Количество чисел, кратных 5:", count(array, 5))
print("Количество чисел, кратных 3 и 5:", array.count('foobar'))
