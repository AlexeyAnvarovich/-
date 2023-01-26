from random import randint
import json


def process():
    n = json.load(open("zorin_alexey_vvod_2.txt", "r"))
    max_sum = 0
    line = -1

    for i in range(len(n)):
        line_sum = 0
        for j in range(len(n[i])):
            if line == i:
                continue

            if n[i][j] % 2 == 0:
                line = i
            else:
                line_sum += my_abs(n[i][j])

        if line_sum > max_sum:
            max_sum = line_sum
            line = i

    file = open("zorin_alexey_vivod_2.txt", "w")
    file.writelines(f"{line},{max_sum}")


def my_abs(a):
    return a if a > 0 else -a


def write_to_file():
    x = generator(int(input("Введите кол-вл строк")), int(input("Введите кол-вл столбцов")),
                  int(input("Введите минимальное значение")), int(input("Введите максимальное значение")))

    file = open("zorin_alexey_vvod_2.txt", "w")
    file.writelines(json.dumps(x))


def generator(row, column, max_value, min_value):
    rowA = []
    for i in range(row):
        columnA = []
        for f in range(column):
            columnA.append(randint(max_value, min_value))

        rowA.append(columnA)

    return rowA


write_to_file()
process()
