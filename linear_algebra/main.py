from from_scratch.vector_operations import add_vectors, subtract_vectors, multiply_vector_by_scalar
from from_scratch.vector_operations import dot_product_vectors, sum_of_squares_vector, magnitude_vector, euclidian_distance_vectors
from from_scratch import Vector

if __name__ == "__main__":
    vectorA: Vector = [1,2,3,4]
    vectorB: Vector = [2,3,4,5]

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