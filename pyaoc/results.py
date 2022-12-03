import argparse
from termcolor import cprint
import sys
from pathlib import Path

def display_results(day : int , part : int) -> None:
    assert isinstance(day,int)
    assert isinstance(part,int)

    ##some hacky code below 😈
    sys.path.insert(0, str(Path.cwd().joinpath(f"day{args.day}")))

    try:
        from solution import PartI , PartII
    except ModuleNotFoundError:
        raise ModuleNotFoundError(cprint("WoOooOOps! It seems your path is messed up!",
                    "red",
                    attrs=["bold","reverse"])) from None

    solution = {1 : PartI , 2 : PartII}.get(args.part)(args.day).solve()
    cprint(f"Printing your individual solution for AoC day I Part {args.part}..." , "blue" , attrs = ["bold"])
    cprint(f"The elf 🧝 found your {solution=}! 🍪", "red" , attrs=["bold", "reverse", "blink"])



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AoC Solutions Day I")
    parser.add_argument("-p" , "--part", type=int, choices=[1, 2], default=1)
    parser.add_argument("-d" , "--day" , type = int , default = 1)
    args = parser.parse_args()
    display_results(args.day , args.part)
