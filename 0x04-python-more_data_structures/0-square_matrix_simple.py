#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        return [list(map(lambda x: x**2, x)) for x in matrix]

#  Did not work
#  newmatrix = matrix.copy()
#  for x in newmatrix:
#  newmatrix = [y*y for y in x]
#  return list(newmatrix)

#  Below also works
#  return [[x ** 2 for x in row] for row in matrix]
