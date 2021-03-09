import data
import math

# function to change the magnitude of a vector by a certain unit
# input: a vector of type Vector and a scalar of type float
# output: a vector of type Vector
def scale_vector(vector: data.Vector, scalar: float)-> data.Vector:
    ret_vector = data.Vector(1,1,1)
    ret_vector.x = vector.x * scalar
    ret_vector.y = vector.y * scalar
    ret_vector.z = vector.z * scalar
    return ret_vector

# function to compute the magnitude of a vector
# input: vector of type Vector
# output: number of type float
def length_vector(vector: data.Vector) ->float:
    sum = vector.x**2 + vector.y**2 + vector.z**2
    return math.sqrt(sum)

# Function to make the magnitude of a vector one
# input: a vector of type Vector
# output: a vector of Vector
def normalize_vector(vector: data.Vector) -> data.Vector:
    length_inverse = 1/(length_vector(vector))
    result = scale_vector(vector, length_inverse)
    return result

# Function to translate in space
# input: a vector of type Vector and a point of type Point
# output: a point of type Point
def translate_point(point: data.Point, vector: data.Vector) -> data.Point:
    x = vector.x + point.x
    y = vector.y + point.y
    z = vector.z + point.z
    return data.Point(x, y, z)

# Function to determine vector required to translate from one point to another
# input: two point of type Point
# output: a vector of type Vector
def vector_from_to(from_point: data.Point, to_point: data.Point)-> data.Vector:
    return data.Vector(to_point.x - from_point.x, to_point.y - from_point.y, to_point.z - from_point.z)

# Function to find the difference between two vectors
# input: two vector of type Vector
# output: a vector of type Vector
def difference_vector(vector1: data.Vector, vector2: data.Vector) -> data.Vector:
    return data.Vector(vector1.x - vector2.x, vector1.y - vector2.y, vector1.z - vector2.z)

# Function to to compute the dot product of two vectors
# input: two vectors of type Vector
# output: a float number
def dot_vector(vector1: data.Vector, vector2: data.Vector) -> float:
    return (vector1.x * vector2.x) + (vector1.y * vector2.y) + (vector1.z * vector2.z)

