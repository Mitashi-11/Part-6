import sys
import typing
import commandline
import file_funcs
import cast
import data


def main(argv: typing.List[str]):
    arguments = commandline.process_cmdArguments(argv)
    write_file = file_funcs.open_file('image.ppm', 'w')
    cast.cast_all_rays(-10, 10, -7.5, 7.5, 512, 384, data.Point(0, 0, -14), arguments[2], arguments[1], arguments[0], write_file)
    write_file.close()


if __name__ == '__main__':
    main(sys.argv)
