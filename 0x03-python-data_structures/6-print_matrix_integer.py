#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        c = ''
        for row in matrix:
            for i in row:
                if row[0] == i:
                    c = str(i)
                else:
                    c = c + ' ' + str(i)
            print(c)
            c = ''
            
