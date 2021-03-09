import collisions
import data
import typing
import v_math
import auxiliary
import file_funcs
import math


# Function to cast a ray into the entire view rectangle
# Input: maximum x coordinate value of type float
# Input: minimum x coordinate value of type float
# Input: maximum y coordinate value of type float
# Input: minimum y coordinate value of type float
# Input: width of the view of type float
# Input: Height of the view of type float
# Input: Location of the eye of type Point from data
# Input: A list of sphere of type Sphere from data
# Input: Ambient light color of type Color from data
# Input: A light of type Light from data
# Output: None
def cast_all_rays(min_x: float, max_x: float, min_y: float, max_y: float, width: int, height: int, eye_point: data.Point, sphere_list: typing.List[data.Sphere], am_light_color: data.Color, light: data.Light, write_file) -> None:
    print('P3', file=write_file)
    print('512 384', file=write_file)
    print('255', file=write_file)
    grid = auxiliary.generate_grid(min_x, max_x, min_y, max_y, width, height)
    for point in grid:
        vt = v_math.vector_from_to(eye_point, point)
        ray = data.Ray(eye_point, vt)
        internal_color = cast_ray(ray, sphere_list, am_light_color, light, eye_point)
        color = auxiliary.convert_color(internal_color)
        print(color.r, color.g, color.b, file=write_file)


# Function to cast a single ray
# Input: A ray of type Ray from data
# Input: A list of sphere of type Sphere from data
# Input: Ambient light color of type Color from data
# Input: A light of type Light from data
# Input: The position of the eye of type Point from data
# Output: The color of the nearest sphere of type Color from data
def cast_ray(ray: data.Ray, sphere_list: typing.List[data.Sphere], am_light_color: data.Color, light: data.Light, eye_point: data.Point) -> data.Color:
    color = data.Color(1,1,1)
    intersected_spheres = collisions.find_intersection_points(sphere_list, ray)
    if not intersected_spheres:
        return color
    else:
        sphere_point = auxiliary.closest_sphere(intersected_spheres, ray)
        light_components = auxiliary.calculate_light_components(sphere_point, sphere_list, eye_point, light)
        color = auxiliary.calculate_color(sphere_point[0], am_light_color, light_components[0], light_components[1], light)
    return color
