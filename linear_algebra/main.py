from from_scratch import Vector, Matrix
from from_scratch.vector_operations import add_vectors, subtract_vectors, multiply_vector_by_scalar
from from_scratch.vector_operations import dot_product_vectors, sum_of_squares_vector, magnitude_vector, euclidian_distance_vectors
from from_scratch.matrix_operations import shape_matrix, get_row_matrix, get_column_matrix, create_matrix
from from_scratch.matrix_operations import create_identity_matrix

import numpy as np
from from_libs import Vector as NPVector, Matrix as NPMatrix
from from_libs.vector_operations import add_vectors as np_add_vectors, subtract_vectors as np_subtract_vectors
from from_libs.vector_operations import multiply_vector_by_scalar as np_multiply_vector_by_scalar
from from_libs.vector_operations import dot_product_vectors as np_dot_product_vectors, sum_of_squares_vector as np_sum_of_squares_vector
from from_libs.vector_operations import magnitude_vector as np_magnitude_vector, euclidian_distance_vectors as np_euclidian_distance_vectors
from from_libs.matrix_operations import shape_matrix as np_shape_matrix, get_row_matrix as np_get_row_matrix, get_column_matrix as np_get_column_matrix
from from_libs.matrix_operations import create_matrix as np_create_matrix, create_identity_matrix as np_create_identity_matrix

def elements_generation_function(n_row: int, n_column: int) -> float:
    return n_row + n_column

def tests_vector_operations_from_scratch(vectorA: Vector, vectorB: Vector) -> None:

    print(f"Vector1: {vectorA}, Vector2: {vectorB}")

    vectors_sum_truth = [3,5,7,9]
    vectors_sum = add_vectors(vectors=[vectorA, vectorB])
    assert vectors_sum == vectors_sum_truth, "vectors addiction is wrong!"
    print(f"add(Vector1, Vector2) = {vectors_sum}")

    vectors_sub_truth = [-1,-1,-1,-1]
    vectors_sub = subtract_vectors(vectorA=vectorA, vectorB=vectorB)
    assert vectors_sub == vectors_sub_truth, "vectors subtraction is wrong!"
    print(f"subtract(Vector1, Vector2) = {vectors_sub}")

    scalar = 2
    prod_scalar_truth = [2,4,6,8]
    prod_scalar = multiply_vector_by_scalar(vector=vectorA, scalar=scalar)
    assert prod_scalar == prod_scalar_truth, "vector product by scalar is wrong!"
    print(f"{scalar} * Vector1 = {prod_scalar}")

    dot_prod_truth = 40
    dot_prod = dot_product_vectors(vectorA=vectorA, vectorB=vectorB)
    assert dot_prod == dot_prod_truth, "vectors dot product is wrong!"
    print(f"dot(Vector1, Vector2) = {dot_prod}")

    sum_squares_truth = 30
    sum_squares = sum_of_squares_vector(vector=vectorA)
    assert sum_squares == sum_squares_truth, "vector sum of squares is wrong!"
    print(f"sum_squares(Vector1) = dot(Vector1, Vector1) = {sum_squares}")

    magnitude_truth = 5.477225575051661
    magnitude = magnitude_vector(vector=vectorA)
    assert magnitude == magnitude_truth, "vector magnitude is wrong!"
    print(f"|Vector1| = {magnitude}")

    distance_truth = 2
    distance = euclidian_distance_vectors(vectorA=vectorA, vectorB=vectorB)
    assert distance == distance_truth, "vectors distance is wrong!"
    print(f"euclidian_distance(Vector1, Vector2) = {distance}")

def tests_matrix_operations_from_scratch(matrixA: Matrix) -> None:
    print(f"Matrix 1:", matrixA)

    shape_truth = (2,4)
    shape = shape_matrix(matrix=matrixA)
    assert shape == shape_truth, "The shape function is wrong!"
    print(f"The shape of Matrix1 is: {shape}")

    row_number = 1
    row_truth = vectorB
    row = get_row_matrix(matrix=matrixA, row_number=row_number)
    assert row == row_truth, "The get row function is wrong!"
    print(f"The {row_number}-th row is: {row}")

    column_number = 2
    column_truth = [3,4]
    column = get_column_matrix(matrix=matrixA, column_number=column_number)
    assert column == column_truth, "The get column function is wrong!"
    print(f"The {column_number}-th column is: {column}")

    n_rows = 2
    n_columns = 2
    created_matrix_truth = [[0,1],[1,2]]
    created_matrix = create_matrix(n_rows=n_rows, n_columns=n_columns, elements_generation_funcion=elements_generation_function)
    assert created_matrix == created_matrix_truth, "The create matrix function is wrong!"
    print(f"The {n_rows} x {n_columns} created matrix is: {created_matrix}")

    n_rows = 3
    identity_matrix_truth = [[1,0,0],[0,1,0],[0,0,1]]
    identity_matrix = create_identity_matrix(n_rows=n_rows)
    assert identity_matrix == identity_matrix_truth, "The create identity matrix function is wrong!"
    print(f"The {n_rows} x {n_rows} identity matrix is: {identity_matrix}")

def tests_vector_operations_from_libs(vectorA: NPVector, vectorB: NPVector) -> None:
    print(f"Vector1: {vectorA}, Vector2: {vectorB}")

    vectors_sum_truth = np.asarray([3,5,7,9], dtype="float")
    vectors_sum = np_add_vectors(vectors=np.asarray([vectorA, vectorB], dtype="float"))
    assert all(vectors_sum == vectors_sum_truth), "vectors addiction is wrong!"
    print(f"add(Vector1, Vector2) = {vectors_sum}")

    vectors_sub_truth = np.asarray([-1,-1,-1,-1], dtype="float")
    vectors_sub = np_subtract_vectors(vectorA=vectorA, vectorB=vectorB)
    assert all(vectors_sub == vectors_sub_truth), "vectors subtraction is wrong!"
    print(f"subtract(Vector1, Vector2) = {vectors_sub}")

    scalar = 2
    prod_scalar_truth = np.asarray([2,4,6,8], dtype="float")
    prod_scalar = np_multiply_vector_by_scalar(vector=vectorA, scalar=scalar)
    assert all(prod_scalar == prod_scalar_truth), "vector product by scalar is wrong!"
    print(f"{scalar} * Vector1 = {prod_scalar}")

    dot_prod_truth = 40
    dot_prod = np_dot_product_vectors(vectorA=vectorA, vectorB=vectorB)
    assert dot_prod == dot_prod_truth, "vectors dot product is wrong!"
    print(f"dot(Vector1, Vector2) = {dot_prod}")

    sum_squares_truth = 30
    sum_squares = np_sum_of_squares_vector(vector=vectorA)
    assert sum_squares == sum_squares_truth, "vector sum of squares is wrong!"
    print(f"sum_squares(Vector1) = dot(Vector1, Vector1) = {sum_squares}")

    magnitude_truth = 5.477225575051661
    magnitude = np_magnitude_vector(vector=vectorA)
    assert magnitude == magnitude_truth, "vector magnitude is wrong!"
    print(f"|Vector1| = {magnitude}")

    distance_truth = 2
    distance = np_euclidian_distance_vectors(vectorA=vectorA, vectorB=vectorB)
    assert distance == distance_truth, "vectors distance is wrong!"
    print(f"euclidian_distance(Vector1, Vector2) = {distance}")

def tests_matrix_operations_from_libs(matrixA: NPMatrix) -> None:
    print(f"Matrix 1:", matrixA)

    shape_truth = (2,4)
    shape = np_shape_matrix(matrix=matrixA)
    assert shape == shape_truth, "The shape function is wrong!"
    print(f"The shape of Matrix1 is: {shape}")

    row_number = 1
    row_truth = vectorB
    row = np_get_row_matrix(matrix=matrixA, row_number=row_number)
    assert all(row == row_truth), "The get row function is wrong!"
    print(f"The {row_number}-th row is: {row}")

    column_number = 2
    column_truth = [3,4]
    column = np_get_column_matrix(matrix=matrixA, column_number=column_number)
    assert all(column == column_truth), "The get column function is wrong!"
    print(f"The {column_number}-th column is: {column}")

    n_rows = 2
    n_columns = 2
    created_matrix_truth = np.asarray([[0,1],[1,2]], dtype="float")
    created_matrix = np_create_matrix(n_rows=n_rows, n_columns=n_columns, elements_generation_funcion=elements_generation_function)
    assert np.all(created_matrix == created_matrix_truth), "The create matrix function is wrong!"
    print(f"The {n_rows} x {n_columns} created matrix is: {created_matrix}")

    n_rows = 3
    identity_matrix_truth = np.asarray([[1,0,0],[0,1,0],[0,0,1]], dtype="float")
    identity_matrix = np_create_identity_matrix(n_rows=n_rows)
    assert np.all(identity_matrix == identity_matrix_truth), "The create identity matrix function is wrong!"
    print(f"The {n_rows} x {n_rows} identity matrix is: {identity_matrix}")

if __name__ == "__main__":
    vectorA: Vector = [1,2,3,4]
    vectorB: Vector = [2,3,4,5]
    matrixA: Matrix = [vectorA, vectorB]

    tests_vector_operations_from_scratch(vectorA=vectorA, vectorB=vectorB)
    tests_matrix_operations_from_scratch(matrixA=matrixA)
    
    vectorA: NPVector = np.asarray(vectorA, dtype="float")
    vectorB: NPVector = np.asarray(vectorB, dtype="float")
    matrixA: NPMatrix = np.asarray(matrixA, dtype="float")

    tests_vector_operations_from_libs(vectorA=vectorA, vectorB=vectorB)
    tests_matrix_operations_from_libs(matrixA=matrixA)

    

    

