import fileinput

def recover_calibration(line: str):
    first = first_digit(line)
    last = first_digit(reversed(line))
    return 10 * first + last

def first_digit(line: str):
    return int(next(c for c in line if c.isdigit()))

if __name__ == "__main__":
    total = 0
    for line in fileinput.input():
        total += recover_calibration(line)
    print(total)
