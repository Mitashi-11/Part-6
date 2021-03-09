import commandline
import cast
import auxiliary
import collisions
import unittest
import data


class CommandLine_Tests(unittest.TestCase):
    def test1(self):
        result = commandline.process_cmdArguments(['', 'test_file', '-ambient', '0.9', '0.9', '0.9'])
        sphere1 = data.Sphere(data.Point(1,1,0), 2, data.Color(1,0,1), data.Finish(0.2, 0.4, 0.5, 0.05))
        sphere2 = data.Sphere(data.Point(8,-10,110), 100, data.Color(0.2, 0.2, 0.6), data.Finish(0.4, 0.8,0, 0.05))
        check = (data.Light(data.Point(-100, 100, -100), data.Color(1.5, 1.5, 1.5)), data.Color(0.9, 0.9, 0.9), [sphere1, sphere2])
        self.assertEqual(result, check)


class Cast_Tests(unittest.TestCase):
    def test_cast_ray1(self):
        spheres = [data.Sphere(data.Point(0.0, 2.0, 0.0), 1.0, data.Color(1, 0, 0), data.Finish(0.5, 0.4, 0.5, 0.05)),
                   data.Sphere(data.Point(0.0, 5.0, 0.0), 1.0, data.Color(0, 0, 1), data.Finish(0.5, 0.4, 0.5, 0.05)),
                   data.Sphere(data.Point(0.0, -4.0, 0.0), 1.0, data.Color(0, 1, 0), data.Finish(0.5, 0.4, 0.5, 0.05)),
                   data.Sphere(data.Point(0.0, 8.0, 0.0), 1.0, data.Color(0, 0, 0), data.Finish(0.5, 0.4, 0.5, 0.05))]
        ray = data.Ray(data.Point(0.0, 0.0, 0.0), data.Vector(0.0, 1.0, 0.0))
        result = cast.cast_ray(ray, spheres, data.Color(1,1,1), data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5,1.5,1.5)), data.Point(0,0,-14))
        self.assertEqual(result, data.Color(0.5, 0.0, 0.0))

    def test_cast_ray2(self):
        spheres = [data.Sphere(data.Point(6.0, 0.0, 0.0), 1.0, data.Color(1, 0, 0), data.Finish(0.5, 0.4, 0.5, 0.05)),
                   data.Sphere(data.Point(0.0, 5.0, 0.0), 1.0, data.Color(0, 0, 1), data.Finish(0.5, 0.4, 0.5, 0.05)),
                   data.Sphere(data.Point(0.0, -4.0, 0.0), 1.0, data.Color(0, 1, 0), data.Finish(0.5, 0.4, 0.5,0.05)),
                   data.Sphere(data.Point(0.0, 8.0, 0.0), 1.0, data.Color(0, 0, 0), data.Finish(0.5, 0.4, 0.5, 0.05))]
        ray = data.Ray(data.Point(0.0, 0.0, 0.0), data.Vector(0.0, 1.0, 0.0))
        result = cast.cast_ray(ray, spheres, data.Color(1,1,1), data.Light(data.Point(-100.0, 100.0, -100.0),data.Color(1.5,1.5,1.5)), data.Point(0,0,-14))
        self.assertEqual(result, data.Color(0, 0, 0.5))


class Tests_auxiliary(unittest.TestCase):
    def test_grid1(self):
        result = auxiliary.generate_grid(-4, 4, -2, 2, 4, 2)
        check = [data.Point(-4, 2, 0), data.Point(-2, 2, 0), data.Point(0, 2, 0), data.Point(2, 2, 0),
                 data.Point(-4, 0, 0), data.Point(-2, 0, 0), data.Point(0, 0, 0), data.Point(2, 0, 0)]
        self.assertEqual(result, check)

    def test_grid2(self):
        result = auxiliary.generate_grid(0, 5, 0, 5, 5, 2)
        check = [data.Point(0, 5, 0), data.Point(1, 5, 0), data.Point(2, 5, 0), data.Point(3, 5, 0),
                 data.Point(4, 5, 0), data.Point(0, 2.5, 0), data.Point(1, 2.5, 0), data.Point(2, 2.5, 0),
                 data.Point(3, 2.5, 0), data.Point(4, 2.5, 0)]
        self.assertEqual(result, check)

    def test_closestSphere1(self):
        spheres = [data.Sphere(data.Point(0.0, 2.0, 0.0), 1.0, data.Color(1, 0, 0), data.Finish(0.5, 0.4, 0.5, 0.05)),
                   data.Sphere(data.Point(0.0, 5.0, 0.0), 1.0, data.Color(0, 0, 1), data.Finish(0.5, 0.4, 0.5, 0.05)),
                   data.Sphere(data.Point(0.0, 4.0, 0.0), 1.0, data.Color(0, 1, 0), data.Finish(0.5, 0.4, 0.5, 0.05)),
                   data.Sphere(data.Point(0.0, 8.0, 0.0), 1.0, data.Color(0, 0, 0), data.Finish(0.5, 0.4, 0.5, 0.05))]
        ray = data.Ray(data.Point(0.0, 0.0, 0.0), data.Vector(0.0, 1.0, 0.0))
        intersected_spheres = collisions.find_intersection_points(spheres, ray)
        result = auxiliary.closest_sphere(intersected_spheres, ray)
        check = (data.Sphere(data.Point(0.0, 2.0, 0.0), 1.0, data.Color(1, 0, 0), data.Finish(0.5, 0.4, 0.5, 0.05)), data.Point(0,1,0))
        self.assertEqual(result, check)

    def test_closestSphere2(self):
        spheres = [data.Sphere(data.Point(6.0, 0.0, 0.0), 1.0, data.Color(1, 0, 0), data.Finish(0.5, 0.4, 0.5, 0.05)),
                   data.Sphere(data.Point(0.0, 5.0, 0.0), 1.0, data.Color(0, 0, 1), data.Finish(0.5, 0.4, 0.5, 0.05)),
                   data.Sphere(data.Point(0.0, -4.0, 0.0), 1.0, data.Color(0, 1, 0), data.Finish(0.5, 0.4, 0.5, 0.05)),
                   data.Sphere(data.Point(0.0, 8.0, 0.0), 1.0, data.Color(0, 0, 0), data.Finish(0.5, 0.4, 0.5, 0.05))]
        ray = data.Ray(data.Point(0.0, 0.0, 0.0), data.Vector(0.0, 1.0, 0.0))
        intersected_spheres = collisions.find_intersection_points(spheres, ray)
        result = auxiliary.closest_sphere(intersected_spheres, ray)
        check = (data.Sphere(data.Point(0.0, 5.0, 0.0), 1.0, data.Color(0, 0, 1), data.Finish(0.5, 0.4, 0.5, 0.05)), data.Point(0,4,0))
        self.assertEqual(result,check)

    def test_calculateColor1(self):
        result = auxiliary.calculate_color(data.Sphere(data.Point(0.0, 5.0, 0.0), 1.0, data.Color(0, 0, 1), data.Finish(0.5, 0.4, 0.5, 0.05)), data.Color(1,1,1), 1, 1, data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5,1.5,1.5)))
        check = data.Color(0.75,0.75,1.85)
        self.assertEqual(result, check)

    def test_calculateColor2(self):
        result = auxiliary.calculate_color(data.Sphere(data.Point(0.0, 2.0, 0.0), 1.0, data.Color(1, 1, 1), data.Finish(0.5, 0.4, 0.5, 0.05)), data.Color(1,1,1), 1, 1, data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5,1.5,1.5)))
        check = data.Color(1.85,1.85,1.85)
        self.assertEqual(result,check)

    def test_convertColor1(self):
        result = auxiliary.convert_color(data.Color(1,1,1))
        check = data.Color(255,255,255)
        self.assertEqual(result, check)

    def test_convertColor2(self):
        result = auxiliary.convert_color(data.Color(0.1,0.1,0.1))
        check = data.Color(25,25,25)
        self.assertEqual(result, check)

    def test_distanceBetweenPoints1(self):
        result = auxiliary.distance_between_points(data.Point(0,0,0), data.Point(1,0,0))
        check = 1
        self.assertEqual(result, check)

    def test_distanceBetweenPoints2(self):
        result = auxiliary.distance_between_points(data.Point(0,0,0), data.Point(0,0,0))
        check = 0
        self.assertEqual(result, check)

    def test_comuptePe1(self):
        result = auxiliary.compute_Pe((data.Sphere(data.Point(0.0, 0.0, 0.0), 1.0, data.Color(1, 1, 1), data.Finish(0.5, 0.4, 0.5, 0.05)), data.Point(0,1,0)))
        check = data.Point(0,1.01,0)
        self.assertEqual(result,check)

    def test_computePe2(self):
        result = auxiliary.compute_Pe((data.Sphere(data.Point(0.0, 2.0, 0.0), 1.0, data.Color(1, 1, 1), data.Finish(0.5, 0.4, 0.5, 0.05)), data.Point(0,1,0)))
        check = data.Point(0, 0.99, 0)
        self.assertEqual(result,check)

    def test_calculate_light_component1(self):
        spheres = [data.Sphere(data.Point(1,1,0),2,data.Color(0,0,1), data.Finish(0.2, 0.4, 0.5, 0.05)), data.Sphere(data.Point(0.5,1.5,-3), 0.5, data.Color(1,0,0), data.Finish(0.2, 0.4, 0.5, 0.05))]
        intersection_pt = collisions.sphere_intersection_point(data.Ray(data.Point(0,0,-14), data.Vector(0.5, 1.5, 11)), data.Sphere(data.Point(1,1,0),2,data.Color(0,0,1), data.Finish(0.2, 0.4, 0.5, 0.05)))
        eye_pt = data.Point(0, 0, -14)
        light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
        result = auxiliary.calculate_light_components((data.Sphere(data.Point(1,1,0),2,data.Color(0,0,1), data.Finish(0.2, 0.4, 0.5, 0.05)),intersection_pt), spheres, eye_pt, light)
        check = (0.8449364794884124, 0.9607772324334302)
        self.assertEqual(result, check)

    def test_calculate_light_component2(self):
        spheres = [data.Sphere(data.Point(1,1,0),2,data.Color(0,0,1), data.Finish(0.2, 0.4, 0.5, 0.05)), data.Sphere(data.Point(0.5,1.5,-3), 0.5, data.Color(1,0,0), data.Finish(0.2, 0.4, 0.5, 0.05))]
        intersection_pt = collisions.sphere_intersection_point(data.Ray(data.Point(0,0,-14), data.Vector(0.5, 1.5, 11)), data.Sphere(data.Point(0.5,1.5,-3), 0.5, data.Color(1,0,0), data.Finish(0.2, 0.4, 0.5, 0.05)))
        eye_pt = data.Point(0, 0, -14)
        light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
        result = auxiliary.calculate_light_components((data.Sphere(data.Point(0.5,1.5,-3), 0.5, data.Color(1,0,0), data.Finish(0.2, 0.4, 0.5, 0.05)), intersection_pt), spheres, eye_pt, light)
        check = (0.5082198628016603, 0.5082198628016605)
        self.assertEqual(result, check)

    def test_compute_specular_intensity1(self):
        eye_pt = data.Point(0,0,-14)
        Pe = data.Point(0.47705401519604174, 1.4311620455881253, -3.5048116656870825)
        normal = data.Vector(-0.04499212706658469, -0.13497638119975397, -0.98982654648647)
        L_dir = data.Vector(-0.5887765593901371, 0.5775947735794256, -0.5654435785566279)
        normal_Ldir = 0.5082198628016603
        result = auxiliary.compute_specular_intensity(Pe, normal, L_dir, normal_Ldir, eye_pt)
        check = 0.5082196122911
        self.assertAlmostEqual(result, check)

    def test_compute_specular_intensity2(self):
        eye_pt = data.Point(0,0,-14)
        Pe = data.Point(0.5507345333286873, 1.6622035998606193, -1.843840267688793)
        normal = data.Vector(-0.22351515756871967, 0.3294545272938401, -0.9173334665118366)
        L_dir = data.Vector(-0.5862702247202266, 0.5733674871854466, -0.5723084380341965)
        normal_Ldir = 0.8449364794884124
        result = auxiliary.compute_specular_intensity(Pe, normal, L_dir, normal_Ldir, eye_pt)
        check = 0.96077723243
        self.assertAlmostEqual(result, check)


class Tests_classes(unittest.TestCase):
    def test_color1(self):
        result = data.Color(0, 10, 100)
        self.assertEqual(result.r, 0)
        self.assertEqual(result.g, 10)
        self.assertEqual(result.b, 100)

    def test_color2(self):
        color1 = data.Color(21, 45, 255)
        color2 = data.Color(21, 45, 255)
        self.assertEqual(color1, color2)

    def test_finish1(self):
        finish1 = data.Finish(0.5,0.4, 0.5, 0.05)
        finish2 = data.Finish(0.5,0.4, 0.5, 0.05)
        self.assertEqual(finish1,finish2)

    def test_finish2(self):
        result = data.Finish(0.5,0.4, 0.5, 0.05)
        self.assertAlmostEqual(result.ambient,0.5)
        self.assertAlmostEqual(result.diffuse,0.4)
        self.assertAlmostEqual(result.specular, 0.5)
        self.assertAlmostEqual(result.roughness, 0.05)

    def test_light1(self):
        result = data.Light(data.Point(0,0,0), data.Color(1,1,1))
        self.assertEqual(result.pt, data.Point(0,0,0))
        self.assertEqual(result.color, data.Color(1,1,1))

    def test_light2(self):
        light1 = data.Light(data.Point(1,2,3), data.Color(0,0,0))
        light2 = data.Light(data.Point(1,2,3), data.Color(0,0,0))
        self.assertEqual(light1, light2)


if __name__ == '__main__':
    unittest.main()
