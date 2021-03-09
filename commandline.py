import typing
import file_funcs
import data


def process_cmdArguments(args: typing.List[str]) -> typing.Optional[typing.Tuple[data.Light, data.Color, typing.List[data.Sphere]]]:
    light = data.Light(data.Point(-100, 100, -100), data.Color(1.5, 1.5, 1.5))
    ambient = data.Color(1,1,1)
    if len(args) >= 3:
        for idx in range(len(args)):
            try:
                if args[idx] == '-light':
                    light = data.Light(data.Point(float(args[idx+1]), float(args[idx+2]), float(args[idx+3])), data.Color(float(args[idx+4]), float(args[idx+5]), float(args[idx+6])))
            except:
                print('Incorrect format: Default Values for light will be used')
            try:
                if args[idx] == '-ambient':
                    ambient = data.Color(float(args[idx+1]), float(args[idx+2]), float(args[idx+3]))
            except:
                print('Incorrect format: Default Values for ambient light color will be used')
    if len(args) >= 2:
        file_name = args[1]
        sphere_list = file_funcs.read_from_file(file_name)
        return (light, ambient, sphere_list)
    else:
        print("python3 ray_caster.py <filename> [-light x y z r g b] [-ambient r g b]")
        exit(1)


def create_sphere(args: str) -> data.Sphere:
    center = data.Point(float(args[0]), float(args[1]), float(args[2]))
    color = data.Color(float(args[4]), float(args[5]), float(args[6]))
    finish = data.Finish(float(args[7]), float(args[8]), float(args[9]), float(args[10]))
    return data.Sphere(center, float(args[3]), color, finish)



