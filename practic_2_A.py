def func(number):
    y = number // 10
    x = number - (y * 10)

    if y == 0:
        return x

    x += func(y)
    print("Результат:")
    return x


print(func(int(input("\nВведите число:\n"))))
