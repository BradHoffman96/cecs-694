#**************************#
#* Brad Hoffman  *         #
#* CECS 694-02   *         # 
#* Assignment 01 *         # 
#************************* #

import random

row_size = 3
col_size = 3

def kadane(sub_matrix):
    max_here = 0
    max_so_far = 0

    for i in range(len(sub_matrix)):
        max_here = max(max_here + sub_matrix[i], 0)
        max_so_far = max(max_here, max_so_far)

    return max_so_far

def findMaxSubMatrix(matrix):
    max_sum = 0

    for left_col in range(col_size):
        temp = []

        for i in range(len(matrix)):
            temp.append(0)

        for right_col in range(left_col, col_size):
            for i in range(row_size):
                temp[i] +=  matrix[i][right_col]

            current = kadane(temp)
            if current > max_sum:
                max_sum = current 

    print(max_sum)

def main():
    #matrix = [[random.randint(0, 5) for i in range(col_size)] for i in range(row_size)]
    a = [-1, 3, 5]
    b = [-10, -3, 20]
    c = []

    #Create the len(a) * len(b) sized matrix to use for finding the largest sub-matrix
    for i in a:
        row = []
        for j in b:
            row.append(i * j)
        c.append(row)

    findMaxSubMatrix(c)

if __name__ == "__main__":
    main()
