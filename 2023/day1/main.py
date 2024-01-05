import argparse

parser = argparse.ArgumentParser(prog="aoc day 1")
parser.add_argument("-f", "--filename", type=str, required=True)
args = parser.parse_args()

numbers = [
    ("one", 1), 
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5), 
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9),
]


def calibration_value(text: str) -> int:
    """Helper method that extracts first digit and last digit."""
    number_text = []
    idx = -1
    while idx < len(text)-1:
        idx += 1
        # check if digit, simple case, add and move on
        try:
            int(text[idx]) 
            number_text.append(text[idx])
            continue
        except ValueError:
            pass
        

        # this means it wasn't a str, check if spelling, otherwise move on
        for number_spell, digit in numbers:
            # check if there is even enough space for spelling to exist
            if (idx + len(number_spell)) > len(text):
                continue

            # check if current char -> end of string matches, break out of loop if so
            if number_spell == text[idx:idx+len(number_spell)]:
                number_text.append(digit)
                # removing this, because some digits can 'share' letters ie twone = 21
                # idx += len(number_spell)-1
                break
        
    digits = []
    for char in number_text:
        try:
            digit = int(char) 
            digits.append(digit)
        except ValueError:
            continue

    return int("{one}{two}".format(one=digits[0], two=digits[-1]))


def main():
    with open(args.filename, "r") as file:
        lines = file.readlines()
   
    values = []
    for line in lines:
        value = calibration_value(line.rstrip())
        values.append(value)

    print("Calibration total value: ", sum(values)) 


if __name__ == "__main__":
    main()

