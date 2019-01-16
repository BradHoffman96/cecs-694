import random

def main():
    col_a = 2
    col_b = 2
    row_a = 2
    row_b = 2

    matrix_a = [[random.randint(0, 5) for i in range(col_a)] for i in range(row_a)]
    matrix_b = [[random.randint(0, 5) for i in range(col_b)] for i in range(row_b)]
    matrix_c = [[0 for i in range(col_a * row_b)] for i in range(row_a * col_b)]

    print(matrix_a)
    print(matrix_b)
    print(matrix_c)

    #Iterate through the rows of matrix_a
    for i in range(row_a):
        #Iterate through the columns of matrix_a
        for j in range(col_a):
            #Iterate through the rows of matrix_b
            for k in range(row_b):
                #Iterate through the columns of matrix_b
                for l in range(col_a):
                    print(i + k + 1, j + l + 1)

if __name__ == "__main__":
    main()
