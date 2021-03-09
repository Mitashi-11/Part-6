import data
import typing
import v_math
import collisions
import math


# Function to find the distance between two points
# Input: Two points of type Point from data
# Output: A float value
def distance_between_points(pt1: data.Point, pt2: data.Point) -> float:
    return math.sqrt((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2 + (pt1.z - pt2.z) ** 2)


# Function to generate the view rectangle
# Input: maximum x coordinate value of type float
# Input: minimum x coordinate value of type float
# Input: maximum y coordinate value of type float
# Input: minimum y coordinate value of type float
# Input: width of the view of type float
# Input: Height of the view of type float
# Output: A list of points of type Point from data
def generate_grid(min_x: float, max_x: float, min_y: float, max_y: float, width: int, height: int) -> typing.List[data.Point]:
    new_list = []
    dx = (max_x - min_x) / width
    dy = (max_y - min_y) / height
    y = max_y
    while y > min_y:
        x = min_x
        while x < max_x:
            pt = data.Point(x, y, 0)
            new_list.append(pt)
            x += dx
        y -= dy
    return new_list


# Function to calculate the closest sphere from a list of tuples of a sphere and its intersection point
# Input: A list of tuples of spheres of type Sphere from dat and points of type Point from data
# Input: A ray of type Ray from data
# Output: A sphere of type Sphere from data
def closest_sphere(intersected_spheres: typing.List[typing.Tuple[data.Sphere, data.Point]], ray: data.Ray) -> typing.Tuple[data.Sphere, data.Point]:
    min_distance = distance_between_points(intersected_spheres[0][1], ray.pt)
    nearest_sphere = intersected_spheres[0][0]
    for sphere_point in intersected_spheres:
        distance = distance_between_points(sphere_point[1], ray.pt)
        if distance <= min_distance:
            min_distance = distance
            nearest_sphere = sphere_point
    return nearest_sphere


# Function to calculate the color of the intersection point
# Input: A sphere of type Sphere from data
# Input: The ambient light color of type Color from data
# Input: The diffuse color component of type float
# Input: The specular intensity of type float
# Output: The color at the intersection of type Color from data
def calculate_color(sphere: data.Sphere, am_light_color: data.Color, diffuse_component: float, specular_intensity: float, light: data.Light) -> data.Color:
    r = (sphere.color.r * sphere.finish.ambient * am_light_color.r) + (diffuse_component * light.color.r * sphere.color.r * sphere.finish.diffuse) + (light.color.r * sphere.finish.specular * (specular_intensity**(1/sphere.finish.roughness)))
    g = (sphere.color.g * sphere.finish.ambient * am_light_color.g) + (diffuse_component * light.color.g * sphere.color.g * sphere.finish.diffuse) + (light.color.g * sphere.finish.specular * (specular_intensity**(1/sphere.finish.roughness)))
    b = (sphere.color.b * sphere.finish.ambient * am_light_color.b) + (diffuse_component * light.color.b * sphere.color.b * sphere.finish.diffuse) + (light.color.b * sphere.finish.specular * (specular_intensity**(1/sphere.finish.roughness)))
    return data.Color(r, g, b)


# Function to convert color arguments from the internal format to the ppm P3 format
# Input: The color to be converted of type Color from data
# Output: The color that it is converted to of type Color from data
def convert_color(color: data.Color) -> data.Color:
    ppm_r = int(color.r * 255)
    ppm_g = int(color.g * 255)
    ppm_b = int(color.b * 255)
    if ppm_r > 255:
        ppm_r = 255
    if ppm_b > 255:
        ppm_b = 255
    if ppm_g > 255:
        ppm_g = 255
    return data.Color(ppm_r, ppm_g, ppm_b)


# Function to calculate P epsilon, a point just off of the sphere
# Input: A sphere of type Sphere from data
# Input: A point which is the intersection point to that sphere of type Point from data
# Output: A point of type Point from data
def compute_Pe(sphere_point: typing.Tuple[data.Sphere, data.Point]) -> data.Point:
    normal = collisions.sphere_normal_at_point(sphere_point[0], sphere_point[1])
    scaled = v_math.scale_vector(normal, 0.01)
    Pe = v_math.translate_point(sphere_point[1], scaled)
    return Pe


# Function to compute the specular intensity of a sphere
# Input: A point Pe of type Point from data
# Input: Normal to the sphere of type Vector from data
# Input: Light's direction vector of type Vector from data
# Input Dot product of type float
# Input: The eye position of type Point from data
# Output: A float value that represents the dot product
def compute_specular_intensity(Pe: data.Point, normal: data.Vector, L_dir: data.Vector, normal_Ldir: float, eye_point: data.Point) -> float:
    intermediate_vector = v_math.scale_vector(normal, (normal_Ldir*2))
    reflection_vector = v_math.difference_vector(L_dir, intermediate_vector)
    V_dir = v_math.normalize_vector(v_math.vector_from_to(eye_point, Pe))
    specular_intensity = v_math.dot_vector(reflection_vector, V_dir)

    if specular_intensity > 0:
        return specular_intensity
    else:
        return 0


# Function to compute the diffuse compunent which is the dot product of a normal at the sphere's intersection point and light's direction vector
# Input: A sphere of type Sphere from data
# Input: Intersection point of type point from data
# Input: A list of sphere of type Sphere from data
# Input: The eye position of type Point from data
# Input: A light ray of type light from data
# Output: A float value that represents the dot product
def calculate_light_components(sphere_point: typing.Tuple[data.Sphere, data.Point], spheres_list: typing.List[data.Sphere], eye_point: data.Point, light: data.Light) -> typing.Tuple[float, float]:
    Pe = compute_Pe(sphere_point)
    normal = collisions.sphere_normal_at_point(sphere_point[0], sphere_point[1])
    L_dir = v_math.normalize_vector(v_math.vector_from_to(Pe, light.pt))
    L_ray = data.Ray(Pe, L_dir)

    for other_sphere in spheres_list:
        if other_sphere is not sphere_point[0]:
            L_ray_intersection = collisions.sphere_intersection_point(L_ray, other_sphere)
            if L_ray_intersection:
                distance_sphere = distance_between_points(Pe, L_ray_intersection)
                distance_light = distance_between_points(Pe, light.pt)
                if distance_sphere < distance_light:
                    return (0, 0)

    normal_Ldir = v_math.dot_vector(normal, L_dir)

    if normal_Ldir > 0:
        specular_intensity = compute_specular_intensity(Pe, normal, L_dir, normal_Ldir, eye_point)
        return (normal_Ldir, specular_intensity)
    else:
        return (0, 0)
