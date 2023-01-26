n = [[1, 3, 5],
     [1, 2, 3],
     [5, 7, 9]]


def func():
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

    print(f"{line}, {max_sum}")


def my_abs(a):
    return a if a > 0 else -a


func()
