from from_scratch.vector_operations import (add_vectors, subtract_vectors, add_multiple_vectors,
                                            multiply_vector_by_scalar, elementwise_mean_multiple_vectors,
                                            dot_product_vectors, sum_of_square_vector, magnitude_vector,
                                            squared_distance_vectors)
from from_scratch import Vector

if __name__ == "__main__":
    vectorA: Vector = [1,2,3,4]
    vectorB: Vector = [2,3,4,5]

    print(f"The sum of the vectors is: {add_vectors(vectorA=vectorA, vectorB=vectorB)}")
    print(f"The subtraction of the vectors is: {subtract_vectors(vectorA=vectorA, vectorB=vectorB)}")
    print(f"The sum of the multiple vectors is: {add_multiple_vectors(vectors=[vectorA, vectorB])}")
    print(f"The product of the vector by scalar is: {multiply_vector_by_scalar(vector=vectorA, scalar=3)}")
    print(f"The mean of the vectors is: {elementwise_mean_multiple_vectors(vectors=[vectorA, vectorB])}")
    print(f"The dot product of the vectors is: {dot_product_vectors(vectorA=vectorA, vectorB=vectorB)}")
    print(f"The sum of square of the vector is: {sum_of_square_vector(vector=vectorA)}")
    print(f"The magnitude of the vector is: {magnitude_vector(vector=vectorA)}")
    print(f"The squared distance between the vectors is: {squared_distance_vectors(vectorA=vectorA, vectorB=vectorB)}")