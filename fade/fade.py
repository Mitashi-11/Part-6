from typing import List
import math
import file_funcs


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
    distance = math.sqrt((row - pixel_row)**2 + (col - pixel_col)**2)
    scale = (radius-distance)/radius
    if scale < 0.2:
        scale = 0.2
    red = pixel[0] * scale
    green = pixel[1] * scale
    blue = pixel[2] * scale
    print(red, green, blue, file=write_file)


def read_file(ifile, ofile, row, col, radius):
    pixel = []
    ctr = 0
    line_ctr = 1
    pixel_row = 0
    pixel_col = 0
    width = 0
    for line in ifile:
        split_line = line.split()
        if line_ctr == 2:
            width = split_line[0]
            height = split_line[1]
            print('P3', file=ofile)
            print(width, height, file=ofile)
            print('255', file=ofile)
        line_ctr += 1
        for value in split_line:
            try:
                pixel.append(int(value))
                ctr += 1
                pixel_col += 1
                if pixel_col == width:
                    pixel_row += 1
                    pixel_col = 0
            except ValueError:
                pass
            if ctr == 3:
                create_fade(pixel, ofile, row, col, radius, pixel_row, pixel_col)
                ctr = 0
                pixel = []
