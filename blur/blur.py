from typing import List
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


def create_blur(pixels, write_file, neighbour_reach, width, height):
    for i in range(len(pixels)):
        pixel_x = i // width
        pixel_y = i % width
        sum_r = 0
        sum_g = 0
        sum_b = 0
        ctr = 0
        x_start = pixel_x - neighbour_reach
        x_end = pixel_x + neighbour_reach
        y_start = pixel_y - neighbour_reach
        y_end = pixel_y + neighbour_reach
        if x_start < 0:
            x_start = 0
        if x_end >= height:
            x_end = height
        if y_start < 0:
            y_start = 0
        if y_end >= width:
            y_end = width
        try:
            for x in range(x_start, x_end):
                for y in range(y_start, y_end):
                    sum_r = sum_r + pixels[(x*width)+y][0]
                    sum_g = sum_g + pixels[(x*width)+y][1]
                    sum_b = sum_b + pixels[(x*width)+y][2]
                    ctr += 1
            avg_r = int(sum_r/ctr)
            avg_g = int(sum_g / ctr)
            avg_b = int(sum_b / ctr)
            print(avg_r, avg_g, avg_b, file=write_file)
        except ValueError:
            print("Incorrect format")


def read_file(ifile, ofile, neighbour_reach):
    pixel = []
    pixels = []
    ctr = 0
    file_content = (ifile.read()).split()
    print('P3', file=ofile)
    print(file_content[1], file_content[2], file=ofile)
    print('255', file=ofile)
    width = int(file_content[1])
    height = int(file_content[2])
    for i in range(4, len(file_content)):
        try:
            pixel.append(int(file_content[i]))
            ctr += 1
        except ValueError:
            print("Incorrect format")
        if ctr == 3:
            pixels.append(pixel)
            ctr = 0
            pixel = []
    create_blur(pixels, ofile, neighbour_reach, width, height)


def main(argv: List[str]):
    comdline_args = read_commandline(argv)
    write_file = file_funcs.open_file('blurred.ppm', 'w')
    read_file(comdline_args[0], write_file, comdline_args[1])
    comdline_args[0].close()
    write_file.close()


if __name__ == '__main__':
    main(sys.argv)