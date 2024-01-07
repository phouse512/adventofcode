import argparse
from dataclasses import dataclass
from typing import List, Union


parser = argparse.ArgumentParser(prog="aoc day 3")
parser.add_argument("-f", "--filename", type=str, required=True)
args = parser.parse_args()

symbols = ["*", "#", "+", "-", "$", "/", "\\", "=", "%", "&", "@", "!", "^", "(", ")"]
digit = "0123456789"


@dataclass
class Value:
    x: int
    y: int
    val: str


def _nextval(currx: int, curry: int, lines) -> Union[None, Value]:
    """Helper to find the next value (handles wrap)"""
    end_x = len(lines[0]) - 1
    end_y = len(lines) - 1
    
    # end of y and x, nothing left
    if curry == end_y and currx == end_x:
        return None
    
    # end of x line
    if currx == end_x:
        return Value(x=0, y=curry+1, val=lines[curry+1][0])
    
    # simple case
    return Value(x=currx+1, y=curry, val=lines[curry][currx+1])


def _get_surrounding_values(value: Value, lines) -> List[Value]:
    """Get surrounding values for a given value."""
    end_x = len(lines[0]) - 1
    end_y = len(lines) - 1
    values = []
    
    y_possible = []
    # handle being on x=0
    if value.x == 0:
        x_possible = [0, 1] 
    elif value.x == end_x:
        x_possible = [value.x-1, value.x]
    else:
        x_possible = [value.x-1, value.x, value.x+1]

    # handle being on y=0
    if value.y == 0:
        y_possible = [0, 1]
    elif value.y == end_y:
        y_possible = [value.y-1, value.y]
    else:
        y_possible = [value.y-1, value.y, value.y+1]

    for y in y_possible:
        for x in x_possible:
            # skip middle position, duh
            if x == value.x and y == value.y:
                continue

            values.append(Value(
                x=x,
                y=y,
                val=lines[y][x]
            ))

    return values


def _check_adjacent_symbol(digit_values: List[Value], lines) -> bool:
    """Helper to determine if symbol is adjacent in any way"""
    # for each digit, look around
    for digit in digit_values:
        neighbors = _get_surrounding_values(digit, lines)

        for n in neighbors:
            if n.val in symbols:
                return True

    return False


def get_number(start_x, start_y: int, lines) -> List[Value]:
    """
    Returns a sorted list of values of subcomponents of a larger number. Given a starting search, gets the full number and then returns.
    """
    still_digit = True
    curr_val = Value(x=start_x, y=start_y, val=lines[start_y][start_x])
    valid_numbers = []
    while still_digit:
        # print("curr: ", curr_val)
        # check if number
        if curr_val.val in digit:
            valid_numbers.append(curr_val) 
        else:  # found non-digit, stopping
            still_digit = False

        # for next iteration, move forward
        curr_val = _nextval(curr_val.x, curr_val.y, lines)

        # print("next: ", curr_val)
        if not curr_val:
            break
        
        if curr_val.x == 0:
            break


    return valid_numbers


def parse_schematic(lines):
    """Schematic parser, where lines is a 2d array"""
    # find all the numbers, and their location
    x_pos, y_pos = 0, 0
    part_numbers = []

    for y_idx, _ in enumerate(lines):

        for x_idx, _ in enumerate(lines[y_idx]):

            # skip counters, when needed to move forward
            if x_idx < x_pos or y_idx < y_pos:
                # print("skipping x: ", x_idx, x_pos)
                continue
            # print(lines[y_idx][x_idx])
            
            numbers = get_number(x_idx, y_idx, lines)

            # if not part a current number, move on
            if not numbers:
                # reset the skip counter, as we are back to standard iteration
                x_pos, y_pos = 0, 0
                continue

            # if there is a number starting at this position, log
            print([v.val for v in numbers])
            is_symbol_adjacent = _check_adjacent_symbol(numbers, lines)
            if is_symbol_adjacent:
                part_numbers.append(int("".join([v.val for v in numbers])))

            # skip the next iteration to end of number, no need to look at any digits
            last_val = numbers[-1]
            next_val = _nextval(last_val.x, last_val.y, lines)
            # print("broad next: ", next_val)

            # if at end, we done
            if not next_val:
                return

            # set skip counters based on end of digit, see above
            x_pos, y_pos = next_val.x, next_val.y
        
    
    print(part_numbers)
    print(sum(part_numbers))


def main():
    lines = [line.rstrip() for line in open(args.filename, "r")]
    parse_schematic(lines)




if __name__ == "__main__":
    main()

