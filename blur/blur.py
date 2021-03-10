from typing import List
import math
import file_funcs
import sys


def read_commandline(argv: List[str]):
    neighbour_reach = 4
    if len(argv) == 3:
        file = file_funcs.open_file(argv[1], 'r')
        neighbour_reach = int(argv[2])
    elif len(argv) == 2:
        file = file_funcs.open_file(argv[1], 'r')
    else:
        print("Incorrect input format")
        exit(1)
    return (file, neighbour_reach)


def create_blur(pixels, write_file, neighbour_reach, width):
    for pixel in pixels:
        pixel_x = pixel[1][0]
        pixel_y = pixel[1][1]
        sum_r = 0
        sum_g = 0
        sum_b = 0
        ctr = 0
        try:
            for x in range(pixel_x - neighbour_reach, pixel_x + neighbour_reach):
                for y in range(pixel_y - neighbour_reach, pixel_y + neighbour_reach):
                    sum_r = sum_r + pixels[(x*width)+y][0][0]
                    sum_g = sum_g + pixels[(x*width)+y][0][1]
                    sum_b = sum_b + pixels[(x*width)+y][0][2]
                    ctr += 1
            avg_r = int(sum_r/ctr)
            avg_g = int(sum_g / ctr)
            avg_b = int(sum_b / ctr)
            print(avg_r, avg_g, avg_b, file=write_file)
        except:
            pass


def read_file(ifile, ofile, neighbour_reach):
    pixel = []
    pixels = []
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
            pixel_location = (pixel_row, pixel_col)
            pixels.append((pixel, pixel_location))
            ctr = 0
            pixel = []
            pixel_col += 1
    create_blur(pixels, ofile, neighbour_reach, width)


def main(argv: List[str]):
    comdline_args = read_commandline(argv)
    write_file = file_funcs.open_file('blurred.ppm', 'w')
    read_file(comdline_args[0], write_file, comdline_args[1])
    comdline_args[0].close()
    write_file.close()


if __name__ == '__main__':
    main(sys.argv)