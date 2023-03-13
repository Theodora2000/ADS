import math


def calculateDistance(mat, m, n):
    distance = [[math.inf] * m for i in range(n)]

    # i,j pozicia, na ktorej sme
    for i in range(n):
        for j in range(m):
            # k,l najblizsia stanica S
            for k in range(n):
                for l in range(m):
                    if mat[k][l] == 1:
                        distance[i][j] = min(distance[i][j], abs(i - k) + abs(j - l))

    for i in range(n):
        for j in range(m):
            print(distance[i][j], end=" ")
        print()


if __name__ == "__main__":
    n = 10
    m = 4
    charging_station = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
    ]
    # n = 17
    # m = 4
    charging_station2 = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    # Function call
    calculateDistance(charging_station2, m, n)
