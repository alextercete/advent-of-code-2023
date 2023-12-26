import fileinput
import re

DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def recover_calibration(line: str):
    first = first_digit(line)
    last = last_digit(line)
    return 10 * first + last

def first_digit(line):
    pattern = re.compile("(\d|" + "|".join(DIGITS.keys()) + ")")
    m = re.search(pattern, line)
    return parse_digit(m.group(0))

def last_digit(line):
    pattern = re.compile("(\d|" + "|".join([d[::-1] for d in DIGITS.keys()]) + ")")
    m = re.search(pattern, line[::-1])
    return parse_digit(m.group(0)[::-1])

def parse_digit(value: str):
    return DIGITS[value] if value in DIGITS else int(value)

if __name__ == "__main__":
    total = 0
    for line in fileinput.input():
        total += recover_calibration(line)
    print(total)
