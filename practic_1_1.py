a = [1, 2, 2, 3, 3, 3]


def find_repeated_elements():

    result = "\nПовторяющиеся элементы:\n"
    exceptions = ""

    for i in range(len(a)):
        element = a[i]
        exist_count = a.count(element)

        if exceptions.count(f"{element}") == 0:
            exceptions += f"{element}"
        else:
            continue

        if exist_count > 1:
            result += f"{element} "*exist_count
            result += "\n"

    return result


print(find_repeated_elements())
