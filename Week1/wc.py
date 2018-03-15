import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="display number of chars, words and lines of given file", type=argparse.FileType("r"))
parser.add_argument("-l", help="returns only number of lines of given file", dest='print_lines', action="store_true", default=False)
parser.add_argument("-w", help="returns only number of words of given file", dest='print_words', action="store_true", default=False)
parser.add_argument("-c", help="returns only number of chars of given file", dest='print_chars', action="store_true", default=False)
args = parser.parse_args()


def count_lines(file):
    counter = 0
    file.seek(0)
    for line in file:
        counter += 1
    return counter


def count_chars(file):
    counter = 0
    file.seek(0)
    for line in file:
        counter += len(line)
    return counter


def count_words(file):
    counter = 0
    file.seek(0)
    for line in file:
        in_the_middle_of_word = False
        for letter in line:
            if letter == ' ' and in_the_middle_of_word is True:
                counter += 1
                in_the_middle_of_word = False
            elif not letter.isspace():
                in_the_middle_of_word = True
        if in_the_middle_of_word is True:
            counter += 1
    return counter


def handler(arguments):
    if arguments.print_lines is False and arguments.print_words is False and arguments.print_chars is False:
        arguments.print_lines = True
        arguments.print_words = True
        arguments.print_chars = True
    if arguments.print_chars is True:
        print("Number of characters: %s" % str(count_chars(arguments.file)))
    if arguments.print_lines is True:
        print("Number of lines: %s" % str(count_lines(arguments.file)))
    if arguments.print_words is True:
        print("Number of words: %s" % str(count_words(arguments.file)))
    print(arguments.file.name)


handler(args)