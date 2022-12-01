import argparse
from data_source import Solution
from termcolor import cprint

class PartI(Solution):

    def solve(self) -> int:
        """Part I SolutiooOOOonNNNNnn!"""
        return max(map(lambda s : sum(int(num) for num in s.split("\n")) , self.data.strip().split("\n"*2)))

class PartII(Solution):

    def solve(self) -> int:
        """Part II SolutiOOOnNnNNnN!"""
        return sum(sorted(map(lambda s : sum(int(num) for num in s.split("\n")) , self.data.strip().split("\n"*2)) , reverse = True)[:3])


solutions = {1: PartI, 2: PartII}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AoC Solutions Day I")
    parser.add_argument("--part", type=int, choices=[1, 2], default=1)
    args = parser.parse_args()
    solution = solutions.get(args.part)().solve()
    if args.part == 1:
        cprint(f"The elf 🧝 with maximum cookie cargo carries {solution} calories! 🍪",
            "red",
            attrs=["bold","reverse","blink"])
    else:
        cprint(
            f"The total cookie cargo of the first three elves is 🧝 {solution} calories! 🍪",
            "red",
            attrs=["bold", "reverse", "blink"])
