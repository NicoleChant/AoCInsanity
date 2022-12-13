#from pyaoc.data_source import Solution
from __future__ import annotations
from dataclasses import dataclass

class Solution:

    def __init__(self):
        self.challenge_data = open("../challenge_data/day_13/day_13.txt").read()

@dataclass(slots=True)
class DistressSignal:

    data : list

    def __post_init__(self) -> None:
        #validation check
        assert isinstance(self.data , list)

    def _resolve(self , left : list,  right : list) -> bool | None:
        assert isinstance(left,list) and isinstance(right,list)

        for i in range(max(len(left),len(right))):
            if i > len(left) - 1:
                return True
            elif i > len(right) - 1:
                return False

            l = left[i]
            r = right[i]

            if isinstance(l,int) and isinstance(r,int):
                if l > r:
                    return False
                elif r > l:
                    return True
                else:
                    continue
            elif isinstance(l,list) and isinstance(r,int):
                result = self._resolve(l , [r])
            elif isinstance(l,int) and isinstance(r,list):
                result = self._resolve([l],r)
            elif isinstance(r,list) and isinstance(l,list):
                result = self._resolve(l,r)

            if result is not None:
                return result
        return

    def __lt__(self , signal : DistressSignal) -> bool:
        return self._resolve(self.data , signal.data)

class PartI(Solution):

    def solve(self) -> int:
        return sum(map(lambda x : x[0] + 1 ,
                    filter(lambda pair : pair[1][0] < pair[1][1] ,
                    enumerate(map(lambda pairs : ( DistressSignal(eval(pairs.split("\n")[0])),DistressSignal(eval(pairs.split("\n")[1]) )), self.challenge_data.split("\n"*2))))))

class PartII(PartI):

   def solve(self) -> int:
        rows = [DistressSignal(eval(row)) for row in self.challenge_data.splitlines() if len(row) > 0 ]
        rows.extend([DistressSignal([[2]]),DistressSignal([[6]])])
        from math import prod
        return prod(map(lambda x : x[0] + 1 , filter(lambda x : x[1].data == [[6]] or x[1].data == [[2]] , enumerate(sorted(rows)))))


if __name__=="__main__":
    solution = PartI().solve()
    print(solution)
    solution= PartII().solve()
    print(solution)
