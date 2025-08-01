from from_scratch import Matrix, Vector
from typing import Tuple, Callable

def shape_matrix(matrix: Matrix) -> Tuple[int, int]:
    """Gets the number of rows and columns of a matrix."""

    n_rows = len(matrix)
    n_columns = len(matrix[0]) if matrix else 0
    assert all(len(row) == n_columns for row in matrix), "All rows must have the same number of columns!"

    return n_rows, n_columns

def get_row_matrix(matrix: Matrix, row_number: int) -> Vector:
    """Gets a row from the matrix, given its index."""

    assert len(matrix), "The matrix is empty!"
    assert row_number >= 0 and row_number < len(matrix), "The row number is out of range!"

    return matrix[row_number]

def get_column_matrix(matrix: Matrix, column_number: int) -> Vector:
    """Gets a column from the matrix, given its index."""

    assert len(matrix), "The matrix is empty!"
    assert column_number >= 0 and column_number < len(matrix[0]), "The column number is out of range!"

    column = [row[column_number] for row in matrix]

    return column

def create_matrix(n_rows: int, n_columns: int, elements_generation_funcion: Callable[[int, int], float]) -> Matrix:
    """Creates a matrix given its shape (number of rows and columns) and a function to generate its elements.\n
    The elements_generation_function receives the shape as input and returns a float as result."""

    matrix = [[elements_generation_funcion(row_i, column_j) for column_j in range(n_columns)] for row_i in range(n_rows)]

    return matrix

def create_identity_matrix(n_rows: int) -> Matrix:
    """Creates an identity matrix, given its number of rows."""
    identity_rule = lambda i,j: 1 if i == j else 0
    identity_matrix = create_matrix(n_rows=n_rows, n_columns=n_rows, elements_generation_funcion=identity_rule)

    return identity_matrix