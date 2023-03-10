# import numpy as np

# nabijacie_stanice = np.array(
#     [
#         [0, 0, 0, "S", 0],
#         [0, 0, 0, 0, 0],
#         [0, "S", 0, 0, 0],
#         [0, 0, 0, 0, 0],
#         ["S", 0, 0, 0, 0],
#         [0, 0, "S", 0, "S"],
#     ],
#     dtype=object,
# )

# print(nabijacie_stanice)


def printDistance(mat):
    global n, m
    ans = [[None] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            ans[i][j] = 999999999999

    # i,j pozicia, na ktorej sme
    for i in range(n):
        for j in range(m):
            # k,l najblizsia stanica S
            for k in range(n):
                for l in range(m):
                    if mat[k][l] == 1:
                        ans[i][j] = min(ans[i][j], abs(i - k) + abs(j - l))

    for i in range(n):
        for j in range(m):
            print(ans[i][j], end=" ")
        print()


if __name__ == "__main__":
    n = 6
    m = 5
    mat = [
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1],
    ]

    # Function call
    printDistance(mat)
