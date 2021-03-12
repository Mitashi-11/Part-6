import data
import commandline
import typing


def open_file(file_name: str, mode: str):
    try:
        file = open(file_name, mode)
        return file
    except IOError as e:
        print('{}: {}'. format(file_name, e.strerror))
        exit(1)


def process_read_lines(read_file) -> typing.List[data.Sphere]:
    idx = 0
    sphere_list = []
    for line in read_file:
        split_line = line.split()
        idx += 1
        try:
            if len(split_line) == 11:
                sphere = commandline.create_sphere(split_line)
                sphere_list.append(sphere)
            else:
                print('malformed sphere on line ', idx, ' ... skipping')
        except ValueError:
            print('malformed sphere on line ', idx, ' ... skipping')
    return sphere_list


def read_from_file(file) -> typing.List[data.Sphere]:
    read_file = open_file(file, 'r')

    sphere_list = process_read_lines(read_file)

    read_file.close()

    return sphere_list

if __name__ == '__main__':
    read_from_file('test_file')

