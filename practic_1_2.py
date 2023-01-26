a = [1, 2, 3, 4, 5, 6, 7, 8]


def get_odd_numbers():

    result = "\nНечётные числа по убываю:\n"

    exit_list = []

    a.sort()

    for i in range(len(a)):
        if a[i] % 2 != 0:
            exit_list.append(a[i])

    exit_list.reverse()

    if len(exit_list) > 0:
        result += f"{exit_list}"
    else:
        result += "Нет нечетных чисел"

    return result


print(get_odd_numbers())
