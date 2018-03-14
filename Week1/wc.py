import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="display number of chars, words and letters of given file", type=argparse.FileType("r"))
args = parser.parse_args()

print(args.file)


def count_lines(file):
    counter = 0
    for lines in file:
        counter += 1
    return counter

def count_chars(file)


print(count_lines(args.file))