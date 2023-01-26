c = 1
d = 2

n = [[1, 2, 3],
     [4, 5, 6],
     [1, 2, 3]]


def func():
    result = []

    for i in range(len(n)):
        for j in range(len(n[i])):
            if n[i][j] == c:
                result.append(i)

    print(result)

    for i in range(len(result)):
        for j in range(len(n[result[i]])):
            n[result[i]][j] *= d

    print(n)


func()
