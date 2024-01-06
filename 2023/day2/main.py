import argparse
from dataclasses import dataclass

parser = argparse.ArgumentParser(prog="aoc day 1")
parser.add_argument("-f", "--filename", type=str, required=True)
parser.add_argument("-p", "--power", action="store_true")
args = parser.parse_args()


@dataclass
class PullResult:
    red: int
    green: int
    blue: int


def parse_pull(pull: str) -> PullResult:
    """Parse a single pull."""
    pull_split = pull.split(",")
    if len(pull_split) > 3:
        print(pull_split)
    red, green, blue = 0, 0, 0
    for split in pull_split:
        count, color = split.strip().split(" ")
        count = int(count)
        if color == "blue":
            blue += count
        elif color == "red":
            red += count
        elif color == "green":
            green += count

    return PullResult(
        red=red,
        green=green,
        blue=blue,
    )


def parse_game_line(line: str, min_pull: PullResult, return_power: bool = False) -> int:
    """Parse a single line."""
    title, games = line.split(":")
    game_id = int(title.split(" ")[-1])
    pulls = games.split(";")
    
    red_min, green_min, blue_min = 0, 0, 0
    for pull in pulls:
        result = parse_pull(pull.strip())

        red_min = max(red_min, result.red)
        green_min = max(green_min, result.green)
        blue_min = max(blue_min, result.blue)
    
    if return_power:
        return red_min * green_min * blue_min

    if red_min > min_pull.red or green_min > min_pull.green or blue_min > min_pull.blue:
        return 0

    return game_id


def main():
    with open(args.filename, "r") as file:
        lines = file.readlines()

    min_pull = PullResult(red=12, green=13, blue=14)
    
    total = 0
    for line in lines:
        total += parse_game_line(line.rstrip(), min_pull, return_power=args.power)

    print(total)


if __name__ == "__main__":
    main()

