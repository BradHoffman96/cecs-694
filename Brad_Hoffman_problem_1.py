import random
import numpy as np

def np_tensor_product(matrix_a, matrix_b):
   matrix_c = np.kron(matrix_a, matrix_b)
   print(matrix_c)

def main():
    col_a = 2
    col_b = 2
    row_a = 2
    row_b = 2

    matrix_a = [[random.randint(0, 5) for i in range(col_a)] for i in range(row_a)]
    matrix_b = [[random.randint(0, 5) for i in range(col_b)] for i in range(row_b)]
    matrix_c = [[0 for i in range(col_a * col_b)] for i in range(row_a * row_b)]

    m_a = [
        [1, 2],
        [3, 4]
    ]

    m_b = [
        [0, 5],
        [6, 7]
    ]

    print(m_a)
    print(m_b)
    np_tensor_product(m_a, m_b)

    #Iterate through the rows of matrix_a
    for i in range(0, row_a):
        #Iterate through the columns of matrix_a
        for k in range(0, row_b):
            #Iterate through the rows of matrix_b
            for j in range(0, col_a):
                #Iterate through the columns of matrix_b
                for l in range(0, col_b):
                    matrix_c[i + l + 1][j + k + 1] = matrix_a[i][j] * matrix_b[k][l]

    print(matrix_c)

    for i in range(col_a * col_b):
        print(matrix_c[i])

if __name__ == "__main__":
    main()
