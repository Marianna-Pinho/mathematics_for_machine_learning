from from_scratch import Vector, Matrix
from from_scratch.vector_operations import add_vectors, subtract_vectors, multiply_vector_by_scalar
from from_scratch.vector_operations import dot_product_vectors, sum_of_squares_vector, magnitude_vector, euclidian_distance_vectors
from from_scratch.matrix_operations import shape_matrix, get_row_matrix, get_column_matrix, create_matrix
from from_scratch.matrix_operations import create_identity_matrix

def elements_generation_function(n_row: int, n_column: int) -> float:
    return n_row + n_column

def tests_vector_operations_from_scratch(vectorA, vectorB):

    print(f"Vector1: {vectorA}, Vector2: {vectorB}")

    vectors_sum_truth = [3,5,7,9]
    vectors_sum = add_vectors(vectors=[vectorA, vectorB])
    assert vectors_sum == vectors_sum_truth, "vectors addiction is wrong!"
    print(f"add(Vector1, Vector2) = {vectors_sum}")

    vectors_sub_truth = [-1,-1,-1,-1]
    vectors_sub = subtract_vectors(vectorA=vectorA, vectorB=vectorB)
    assert vectors_sub == vectors_sub_truth, "vectors subtraction is wrong!"
    print(f"subtract(Vector1, Vector2) = {vectors_sub}")

    prod_scalar_truth = [2,4,6,8]
    prod_scalar = multiply_vector_by_scalar(vector=vectorA, scalar=2)
    assert prod_scalar == prod_scalar_truth, "vector product by scalar is wrong!"
    print(f"{2} * Vector1 = {prod_scalar}")

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

def tests_matrix_operations_from_scratch(matrixA):
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

if __name__ == "__main__":
    vectorA: Vector = [1,2,3,4]
    vectorB: Vector = [2,3,4,5]
    matrixA: Matrix = [vectorA, vectorB]

    # tests_vector_operations_from_scratch(vectorA=vectorA, vectorB=vectorB)
    tests_matrix_operations_from_scratch(matrixA=matrixA)
    