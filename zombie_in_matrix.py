'''
Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. Find out how many hours does it take to infect all humans?

Example:

Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

Output: 2

Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]
int minHours(int rows, int columns, List<List<Integer>> grid) {
	//
}
'''


rows = 4
cols = 5

matrix = [
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1]
]


def hours_to_infect(rows_par, cols_par, matrix_par):
    """
    Find how many hours to infect all adjacents 0s
    :param rows_par: integer
    :param cols_par: integer
    :param matrix_par: list
    :return:
    """
    if not rows_par or not cols_par:
        return 0

    directions = [
        [1, 0],  # down
        [-1, 0],  # up
        [0, 1],  # right
        [0, -1]  # left
    ]
    coords_1s = [[i, j] for i in range(rows_par) for j in range(cols_par) if matrix_par[i][j] == 1]
    print(coords_1s)
    time = 0

    while True:
        new_coords1s = []
        for [i, j] in coords_1s:
            for dir in directions:
                ni, nj = i + dir[0], j + dir[1]
                if 0 <= ni < rows_par and 0 <= nj < cols_par and matrix_par[ni][nj] == 0:
                    matrix_par[ni][nj] = 1
                    new_coords1s.append([ni, nj])

        coords_1s = new_coords1s
        if not coords_1s:
            break
        time += 1

    return time


print(hours_to_infect(rows, cols, matrix))
