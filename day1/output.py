import argparse
from elves import PartI , PartII
from termcolor import cprint

solutions = {1: PartI, 2: PartII}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AoC Solutions Day I")
    parser.add_argument("-p" , "--part", type=int, choices=[1, 2], default=1)
    args = parser.parse_args()
    solution = solutions.get(args.part)().solve()
    if args.part == 1:
        cprint(
            f"The elf 🧝 with maximum cookie cargo carries {solution} calories! 🍪",
            "red",
            attrs=["bold", "reverse", "blink"])
    else:
        cprint(
            f"The total cookie cargo of the first three elves is 🧝 {solution} calories! 🍪",
            "red",
            attrs=["bold", "reverse", "blink"])
