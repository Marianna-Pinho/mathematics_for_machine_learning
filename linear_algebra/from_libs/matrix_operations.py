from . import Matrix, Vector
from typing import Tuple, Callable
import numpy as np

def shape_matrix(matrix: Matrix) -> Tuple[int, int]:
    """Gets the number of rows and columns of a matrix."""

    shape = matrix.shape
    assert shape[1], "matrix must have all dimensions well defined!"

    return shape

def get_row_matrix(matrix: Matrix, row_number: int) -> Vector:
    """Gets a row from the matrix, given its index."""

    assert matrix.shape[0], "The matrix is empty!"
    assert row_number >= 0 and row_number <  matrix.shape[0], "The row number is out of range!"

    return matrix[row_number]

def get_column_matrix(matrix: Matrix, column_number: int) -> Vector:
    """Gets a column from the matrix, given its index."""

    assert  matrix.shape[0], "The matrix is empty!"
    assert column_number >= 0 and column_number < matrix.shape[1], "The column number is out of range!"

    return matrix[:, column_number]

def create_matrix(n_rows: int, n_columns: int, elements_generation_funcion: Callable[[int, int], float]) -> Matrix:
    """Creates a matrix given its shape (number of rows and columns) and a function to generate its elements.\n
    The elements_generation_function receives the shape as input and returns a float as result."""

    matrix = np.fromfunction(function=elements_generation_funcion, shape=(n_rows, n_columns), dtype="float")

    return matrix

def create_identity_matrix(n_rows: int) -> Matrix:
    """Creates an identity matrix, given its number of rows."""

    return np.identity(n_rows)