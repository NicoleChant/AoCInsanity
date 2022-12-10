from pyaoc.data_source import Solution
import numpy as np

class PartI(Solution):

    def solve(self):
        data = self.challenge_data.splitlines()
        cycles = 0
        X = 1
        cycle_data = dict()
        for command in data:
            if command == "noop":
                cycles += 1
                cycle_data.update({cycles:X})
            else:
                cycles += 1
                cycle_data.update({cycles:X})
                val = int(command.split(" ")[-1])
                cycles += 1
                cycle_data.update({cycles:X})
                X += val
        return sum(signal*cycle_data[signal] for signal in [20, 60, 100, 140, 180, 220])


class PartII(Solution):

   def solve(self):
        CTR = ""
        data = self.challenge_data.splitlines()
        cycles = 0
        X = 1
        cycle_data = dict()
        for command in data:
            if command == "noop":
                cycles += 1
                cycle_data.update({cycles:X})
            else:
                cycles += 1
                cycle_data.update({cycles:X})
                val = int(command.split(" ")[-1])
                cycles += 1
                cycle_data.update({cycles:X})
                X += val

        CTR = "\n".join("".join("#" if c+1 in [d,d+1,d+2] else "." for c , d in enumerate(list(cycle_data.values())[40*i:40*(i+1)])) for i in range(6))
        return CTR


if __name__ == "__main__":
    solution = PartII().solve()
    print(solution)
