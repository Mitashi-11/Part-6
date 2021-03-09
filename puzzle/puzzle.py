from typing import List
import sys
import file_funcs


def read_commandline(argv: List[str]):
    if len(argv) == 2:
        file = file_funcs.open_file(argv[1], 'r')
        return file
    else:
        print("Incorrect input format")
        exit(1)


def solve_puzzle(pixel: List[float], write_file):
    red = pixel[0] * 10
    if red > 255:
        red = 255
    green = red
    blue = red
    print(red, green, blue, file=write_file)


def read_file(ifile, ofile):
    pixel = []
    ctr = 0
    line_ctr = 1
    for line in ifile:
        split_line = line.split()
        if line_ctr == 2:
            print('P3', file=ofile)
            print(split_line[0], split_line[1], file=ofile)
            print('255', file=ofile)
        line_ctr += 1
        for value in split_line:
            try:
                pixel.append(int(value))
                ctr += 1
            except ValueError:
                pass
            if ctr == 3:
                solve_puzzle(pixel, ofile)
                ctr = 0
                pixel = []


def main(argv: List[str]):
    input_file = read_commandline(argv)
    write_file = file_funcs.open_file('hidden.ppm', 'w')
    read_file(input_file, write_file)
    input_file.close()
    write_file.close()


if __name__ == '__main__':
    main(sys.argv)