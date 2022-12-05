from pyaoc.data_source import Solution
import re
import re

class Preprocessor(Solution):

    def _preprocess(self):
        crates , instructions = self.challenge_data.split("\n"*2)
        crates = ["".join("," if (i+1)%4==0 else c for i , c in enumerate(crate)).split(",")[::-1] for crate in crates.split("\n")[:-1]]
        crates = {str(9-i) : [s[1] for s in stack if len(s.strip())>0] for i , stack in enumerate(zip(*crates[::-1]))}
        return crates , map(lambda instr : re.sub("[^0-9]","",instr) , instructions.split("\n"))

class PartI(Preprocessor):

    def solve(self):
        crates , instructions = self._preprocess()
        for command in instructions:
            number , origin , dest = int(command[:-2]) , command[-2] , command[-1]
            crates[dest].extend(reversed(crates[origin][-number:]))
            crates[origin] = crates[origin][:-number]
        return "".join(val[-1] for val in crates.values())[::-1]

class PartII(Preprocessor):

   def solve(self):
        crates , instructions = self._preprocess()
        for command in instructions:
            number , origin , dest = int(command[:-2]) , command[-2] , command[-1]
            crates[dest].extend(crates[origin][-number:])
            crates[origin] = crates[origin][:-number]
        return "".join(val[-1] for val in crates.values())[::-1]


if __name__=="__main__":
    solution=PartII().solve()
    print(solution)
