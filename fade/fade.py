from typing import List
import math
import file_funcs
import sys


def read_commandline(argv: List[str]):
    if len(argv) == 5:
        file = file_funcs.open_file(argv[1], 'r')
        row = int(argv[2])
        col = int(argv[3])
        radius = int(argv[4])
        return (file, row, col, radius)
    else:
        print("Incorrect input format")
        exit(1)


def create_fade(pixel: List[float], write_file, row, col, radius, pixel_row, pixel_col):
    distance = math.sqrt((pixel_row - row)**2 + (pixel_col - col)**2)
    scale = (radius-distance)/radius
    if scale < 0.2:
        scale = 0.2
    red = int(pixel[0] * scale)
    green = int(pixel[1] * scale)
    blue = int(pixel[2] * scale)
    print(red, green, blue, file=write_file)


def read_file(ifile, ofile, row, col, radius):
    pixel = []
    ctr = 0
    pixel_row = 0
    pixel_col = 0
    file_content = (ifile.read()).split()
    print('P3', file=ofile)
    print(file_content[1], file_content[2], file=ofile)
    print('255', file=ofile)
    width = int(file_content[1])
    for i in range(4, len(file_content)):
        try:
            pixel.append(int(file_content[i]))
            ctr += 1
        except ValueError:
            pass
        if ctr == 3:
            if pixel_col == width:
                pixel_row += 1
                pixel_col = 0
            create_fade(pixel, ofile, row, col, radius, pixel_row, pixel_col)
            ctr = 0
            pixel = []
            pixel_col += 1


def main(argv: List[str]):
    comdline_args = read_commandline(argv)
    write_file = file_funcs.open_file('fadded.ppm', 'w')
    read_file(comdline_args[0], write_file, comdline_args[1], comdline_args[2], comdline_args[3])
    comdline_args[0].close()
    write_file.close()


if __name__ == '__main__':
    main(sys.argv)