from . import Vector
from typing import List
import math


def add_vectors(vectors: List[Vector]) -> Vector:
    """Adds all vectors elements in an element wise manner.\n
    The sum of vectors happens element-wisely. It means that we sum each dimension separately.\n
    EXAMPLE: v = [v1, v2] e u = [u1, u2]. Then, v+u = [v1+u1, v2+u2]"""

    assert len(vectors), "there must be at least one vector provided!"

    vectors_dimension = len(vectors[0])
    assert all(len(v) == vectors_dimension for v in vectors), "all vectors must have the same size!"

    new_vector = [sum([v[j] for v in vectors]) for j in range(vectors_dimension)]

    return new_vector

def subtract_vectors(vectorA: Vector, vectorB: Vector) -> Vector:
    """Substracts vectors elementos in an element wise manner.\n
    The subtraction of vectors happens element-wisely. It means that we subtract each dimension separately.\n
    EXAMPLE: v = [v1, v2] e u = [u1, u2]. Then, v-u = [v1-u1, v2-u2]"""

    assert len(vectorA) == len(vectorB)
    new_vector = [va_i - vb_i for va_i, vb_i in zip(vectorA, vectorB)]

    return new_vector

def multiply_vector_by_scalar(vector: Vector, scalar: float) -> Vector:
    """Multiple each element of the vector by scalar.\n
    When multiplying a vector by a scalar, the scalar mutiplies each dimension of the vector.\n
    EXAMPLE: v = [v1, v2]. Então, 2*v = [2*v1, 2*v2]"""

    return [scalar * element for element in vector]

def dot_product_vectors(vectorA: Vector, vectorB: Vector) -> float:
    """Computes the dot product of two vectors.\n
    The dot product of vectors helps us evaluate the orthogonality among vectors, as well as,
    makes part of similarity computations and neural networks activations math.
    It is the sum of the products of the corresponding dimensions of each vectors, 
    which results in a scalar value: va1*vb1 + va2*vb2 + ... + van*vbn."""

    assert len(vectorA) == len(vectorB), "vectors must be the same size!"

    dot_result = sum(va_i*vb_i for va_i, vb_i in zip(vectorA, vectorB))

    return dot_result

def sum_of_squares_vector(vector: Vector) -> float:
    """Performs the sum of squares of a vector.\n
    Sum of squares if commonly used when we want to compute the magnitude of a vector\n
    EXAMPLE: v = [v1, v2]. Then, |v|^2 =  v1*v1 + v2*v2"""

    return dot_product_vectors(vectorA=vector, vectorB=vector)

def magnitude_vector(vector: Vector) -> float:
    """Computes the magnitude of a vector, which reprents its length.\n
    EXAMPLE: v = [v1, v2]. Then, |v| =  sqrt(v1*v1 + v2*v2)"""

    return math.sqrt(sum_of_squares_vector(vector=vector))

def euclidian_distance_vectors(vectorA: Vector, vectorB: Vector) -> float:
    """Computes the euclidian distance between two vectors, which is the length of the line segment between them.\n
    EXAMPLE: v = [v1, v2], u = [u1, u2]. Then, dist(v,u) = sqrt((v1-u1)^2 + (v2-u2)^2)"""

    line_segment = subtract_vectors(vectorA=vectorA, vectorB=vectorB)
    line_length = magnitude_vector(vector=line_segment)

    return line_length