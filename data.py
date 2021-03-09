# Compare two float values for approximate equality.
# input: first number as float
# input: second number as float
# result: bool indicating approximate equality
def nearly_equal(n: float, m: float) -> bool:
    epsilon = 0.00001
    return (n - epsilon < m) and (n + epsilon > m)


class Finish:
    def __init__(self, ambient: float, diffuse: float, specular: float, roughness: float):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness

    def __eq__(self, other: object) -> bool:
        return (type(other) is Finish
                and nearly_equal(self.ambient, other.ambient)
                and nearly_equal(self.diffuse, other.diffuse)
                and nearly_equal(self.specular, other.specular)
                and nearly_equal(self.roughness, other.roughness))


class Color:
    def __init__(self, r: float, g: float, b: float):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other: object) -> bool:
        return (type(other) is Color
                and nearly_equal(self.r, other.r)
                and nearly_equal(self.g, other.g)
                and nearly_equal(self.b, other.b)
                )


class Point:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other: object) -> bool:
        return (type(other) is Point
                and nearly_equal(self.x, other.x)
                and nearly_equal(self.y, other.y)
                and nearly_equal(self.z, other.z)
                )


class Vector:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other: object) -> bool:
        return (type(other) is Vector
                and nearly_equal(self.x, other.x)
                and nearly_equal(self.y, other.y)
                and nearly_equal(self.z, other.z)
                )


class Ray:
    def __init__(self, pt: Point, dir: Vector):
        self.pt = pt
        self.dir = dir

    def __eq__(self, other: object) -> bool:
        return (type(other) is Ray
                and self.pt == other.pt
                and self.dir == other.dir
                )


class Sphere:
    def __init__(self, center: Point, radius: float, color: Color, finish: Finish):
        self.center = center
        self.radius = radius
        self.color = color
        self.finish = finish

    def __eq__(self, other: object) -> bool:
        return (type(other) is Sphere
                and self.center == other.center
                and nearly_equal(self.radius, other.radius)
                and self.color == other.color
                and self.finish == other.finish
                )


class Light:
    def __init__(self, pt: Point, color: Color):
        self.pt = pt
        self.color = color

    def __eq__(self, other: object) -> bool:
        return (type(other) is Light
                and self.pt == other.pt
                and self.color == other.color)
