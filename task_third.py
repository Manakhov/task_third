def check(x):
    if x % 3 == 0:
        return "foo"
    elif x % 5 == 0:
        return "bar"
    else:
        return x


array = []
i = 1
while i < 101:
    array.append(check(i))
    i = i + 1
print(array)
