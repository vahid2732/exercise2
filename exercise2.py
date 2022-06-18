import numpy as np


def swap(coords):
    # coords[:, 0], coords[:, 1], coords[:, 2], coords[:, 3], = coords[:, 1], coords[:, 1], coords[:, 3], coords[:, 2]

    # The correct way to swap the columns of an array
    # arr[:, [start_index, last_index]] = arr[:, [last_index, start_index]]
    coords[:, [0, 1]], coords[:, [2, 3]] = coords[:, [1, 0]], coords[:, [3, 2]]

    return coords


coords = np.array([[10, 5, 15, 6, 0],
                   [11, 3, 13, 6, 0],
                   [5, 3, 13, 6, 1],
                   [4, 4, 13, 6, 1],
                   [6, 5, 13, 16, 1]])

swapped_coords = swap(coords)
print(swapped_coords)
