import sys


def error_crash(function, line, word, is_debug):
    print(f"An error occured at line: {line}, word: {word}")
    if is_debug:
        print(f"    DEBUG: Error uccored from function {function}")
    sys.exit()


unknown = "|| unknown ||"
