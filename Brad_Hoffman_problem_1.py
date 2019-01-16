
matrix_a = [
        [1, 2],
        [2, 4]
    ]

matrix_b = [
        [3, 2],
        [1, 4]
    ]

def main():
    print(matrix_a)
    print(matrix_b)

    #Iterate through the rows of matrix_a
    for index_row_a, row_a in enumerate(matrix_a):
        #Iterate through the columns of matrix_a
        for index_col_a, item_a in enumerate(row_a):
            #Iterate through the rows of matrix_b
            for index_row_b, row_b in enumerate(matrix_b):
                #Iterate through the columns of matrix_b
                for index_col_b, item_b in enumerate(row_b):
                    print(item_a, item_b)


if __name__ == "__main__":
    main()
