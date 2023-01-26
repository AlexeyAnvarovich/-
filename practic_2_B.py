def func():
    value = int(input("Введите число: "))
    max_value = value

    if value == 0:
        return max_value

    next_value = func()

    if max_value < next_value:

        print("\nНаибольшее значение:")

        max_value = next_value

    return max_value


print(func())
