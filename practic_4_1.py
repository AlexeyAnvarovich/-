from random import randint
import json


def process(c, d):
    n = json.load(open("zorin_alexey_vvod_1.txt", "r"))
    result = []

    for i in range(len(n)):
        for j in range(len(n[i])):
            if n[i][j] == c:
                result.append(i)

    for i in range(len(result)):
        for j in range(len(n[result[i]])):
            n[result[i]][j] *= d

    file = open("zorin_alexey_vivod_1.txt", "w")
    file.writelines(json.dumps(n))


def write_to_file():
    x = generator(int(input("Введите кол-вл строк")), int(input("Введите кол-вл столбцов")),
                  int(input("Введите минимальное значение")), int(input("Введите максимальное значение")))

    file = open("zorin_alexey_vvod_1.txt", "w")
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
process(int(input("Введите искомое число")), int(input("Введите множитель")))
print("====Complite====")
