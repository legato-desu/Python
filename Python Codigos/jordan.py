import numpy as np

def gauss_jordan(x, y, verbose=0):
    m, n = x.shape
    augmented_mat = np.zeros(shape=(m, n + 1))
    augmented_mat[:m, :n] = x
    augmented_mat[:, m] = y
    np.set_printoptions(precision=2, suppress=True)
    if verbose > 0:
        print('# Matriz aumentada')
        print(augmented_mat)
    outer_loop = [[0, m - 1, 1], [m - 1, 0, -1]]
    for d in range(2):
        for i in range(outer_loop[d][0], outer_loop[d][1], outer_loop[d][2]):
            inner_loop = [[i + 1, m, 1], [i - 1, -1, -1]]
            for j in range(inner_loop[d][0], inner_loop[d][1], inner_loop[d][2]):
                k = (-1) * augmented_mat[j, i] / augmented_mat[i, i]
                temp_row = augmented_mat[i, :] * k
                if verbose > 1:
                    print('# Tomamos F%2i y F%2i' % (i + 1, j + 1))
                    print('-> Multiplico = %.2f' % k, '*', augmented_mat[i, :], '=', temp_row,'+', augmented_mat[j, :])
                augmented_mat[j, :] = augmented_mat[j, :] + temp_row
                if verbose > 1:
                    print(augmented_mat)
    for i in range(0, m):
        augmented_mat[i, :] = augmented_mat[i, :] / augmented_mat[i, i]
    if verbose > 0:
        print('# Matriz identidad')
        print(augmented_mat,"//")
    return augmented_mat[:, n]


if __name__ == "__main__":
    coefficients = np.array([[2, 1, -1],
                            [1, 4, 3],
                            [-6, 4, 9]])
    right_hand_side = np.array([-1, 10, 30])
    b = gauss_jordan(coefficients, right_hand_side, 2)
    print("# Los valores de x, y, z son = ",b)