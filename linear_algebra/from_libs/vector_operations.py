import numpy as np
from . import Vector
from numpy.typing import NDArray

def add_vectors(vectors: NDArray[Vector]) -> Vector:
    """Adds all vectors elements in an element wise manner.\n
    The sum of vectors happens element-wisely. It means that we sum each dimension separately.\n
    EXAMPLE: v = [v1, v2] and u = [u1, u2]. Then, v+u = [v1+u1, v2+u2]"""

    assert vectors.shape[0], "there must be at least one vector provided!"

    return np.sum(vectors, axis=0)

def subtract_vectors(vectorA: Vector, vectorB: Vector) -> Vector:
    """Substracts vectors elements in an element wise manner.\n
    The subtraction of vectors happens element-wisely. It means that we subtract each dimension separately.\n
    EXAMPLE: v = [v1, v2] and u = [u1, u2]. Then, v-u = [v1-u1, v2-u2]"""

    assert vectorA.shape == vectorB.shape, "all vectors must have the same size!"

    return vectorA - vectorB

def multiply_vector_by_scalar(vector: Vector, scalar: float) -> Vector:
    """Multiple each element of the vector by a scalar.\n
    When multiplying a vector by a scalar, the scalar mutiplies each dimension of the vector.\n
    EXAMPLE: v = [v1, v2]. Then, 2*v = [2*v1, 2*v2]"""

    return scalar * vector

def dot_product_vectors(vectorA: Vector, vectorB: Vector) -> float:
    """Computes the dot product of two vectors.\n
    It is the sum of the products of the corresponding dimensions of each vector, resulting in a scalar value.\n
    EXAMPLE: v = [v1, v2] and u = [ u1, u2]. Then, dot(v,u) = (v1 * u1) + (v2 * u2)."""

    assert vectorA.shape == vectorB.shape, "all vectors must have the same size!"

    return np.dot(vectorA, vectorB)

def sum_of_squares_vector(vector: Vector) -> float:
    """Performs the sum of squares of a vector.\n
    The sum of squares if commonly used when we want to compute the magnitude of a vector\n
    EXAMPLE: v = [v1, v2]. Then, |v|^2 =  v1*v1 + v2*v2"""

    return dot_product_vectors(vectorA=vector, vectorB=vector)

def magnitude_vector(vector: Vector) -> float:
    """Computes the magnitude of a vector, which reprents its length.\n
    EXAMPLE: v = [v1, v2]. Then, |v| =  sqrt(v1*v1 + v2*v2)"""

    return np.linalg.vector_norm(vector)

def euclidian_distance_vectors(vectorA: Vector, vectorB: Vector) -> float:
    """Computes the euclidian distance between two vectors, which is the length of the line segment between them.\n
    EXAMPLE: v = [v1, v2], u = [u1, u2]. Then, dist(v,u) = sqrt((v1-u1)^2 + (v2-u2)^2)"""

    line_segment = subtract_vectors(vectorA=vectorA, vectorB=vectorB)
    line_length = magnitude_vector(vector=line_segment)

    return line_length