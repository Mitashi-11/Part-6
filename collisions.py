from typing import List, Optional, Tuple
import v_math
import data
import math

# Function to return a normal vector at a point on the surface of a sphere
# input: the sphere of type Sphere from data
# input: the point on the surface of type Point from data
# output: the normal vector of type Vector from data
def sphere_normal_at_point(sphere: data.Sphere, point: data.Point) -> data.Vector:
    center_to_point_vector = v_math.vector_from_to(sphere.center, point)
    result = v_math.normalize_vector(center_to_point_vector)
    return result

# Function that returns all the spheres a given ray intersects along with the points of intersections
# input: a list of spheres of type Sphere from data
# input: the ray to check of type Ray from data
# output: a list of tuples that contain an intersected sphere and the point of intersection
def find_intersection_points(sphere_list: List[data.Sphere], ray: data.Ray) -> List[Tuple[data.Sphere, data.Point]]:
    new_list = []
    for sphere in sphere_list:
        result = sphere_intersection_point(ray, sphere)
        if result != None:
            new_list.append((sphere, result))
    return new_list

# Function to check if a ray intersects a sphere
# input: a sphere of type Sphere from data
# input: a ray of type Ray from data
# output: an optional list of closest point of intersection of the ray and sphere
def sphere_intersection_point(the_ray: data.Ray, the_sphere: data.Sphere) -> Optional[data.Point]:
    difference = v_math.vector_from_to(the_sphere.center, the_ray.pt)
    A = v_math.dot_vector(the_ray.dir, the_ray.dir)
    B = (2 * v_math.dot_vector(difference, the_ray.dir))
    C = v_math.dot_vector(difference, difference) - (the_sphere.radius**2)
    D = (B**2) - (4 * A * C)
    if D >= 0:
        rt1 = (-B + math.sqrt(D))/(A*2)
        rt2 = (-B - math.sqrt(D))/(A*2)
        intersection_pt1 = v_math.translate_point(the_ray.pt, v_math.scale_vector(the_ray.dir, rt1))
        intersection_pt2 = v_math.translate_point(the_ray.pt, v_math.scale_vector(the_ray.dir, rt2))
        distance_vt1 = v_math.vector_from_to(the_ray.pt, intersection_pt1)
        distance_vt2 = v_math.vector_from_to(the_ray.pt, intersection_pt2)
        if rt1 >= 0 and rt2 >= 0:
            if v_math.length_vector(distance_vt1) < v_math.length_vector(distance_vt2):
                return intersection_pt1
            else:
                return intersection_pt2
        elif rt1 >= 0 > rt2:
            return intersection_pt1
        elif rt1 < 0 <= rt2:
            return intersection_pt2
        else:
            return None
    else:
        return None

