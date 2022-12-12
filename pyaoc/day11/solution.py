from __future__ import annotations
from pyaoc.data_source import Solution
from dataclasses import dataclass , field
from typing import ClassVar , Callable
import re
from functools import reduce
from tqdm import tqdm
from operator import mul
import math

@dataclass(slots=True,kw_only=True)
class Monkey:

    num : int
    div_criterion : int
    operate : Callable[[int],int]
    throw_to : tuple[int,int]
    items : list[int] = field(default_factory=list)
    stress_relief : int = 3
    activity : int = field(init = False , default = 0)
    monkeys : ClassVar[dict[Monkey]] = dict()

    def __post_init__(self) -> None:
        Monkey.monkeys.update({self.num:self})

    def add_item(self , item : int) -> None:
        self.items.append(item)

    def _decide(self , item : int) -> int:
        return int(not not item%self.div_criterion)

    def _throw(self , chosen_item : int) -> None:
        modified_anxiety = (self.operate(chosen_item) % math.prod([m.div_criterion for m in Monkey.monkeys.values()])) if self.stress_relief == 1 else self.operate(chosen_item) // self.stress_relief

        monkey_destination = self._decide(modified_anxiety)

        monkey = self.throw_to[monkey_destination]

        Monkey.monkeys[monkey].add_item(modified_anxiety)
        self.activity += 1

    def throw(self) -> None:
        while len(self.items) > 0:
            chosen_item = self.items.pop(0)
            self._throw(chosen_item)

    def __lt__(self , monkey : Monkey) -> Monkey:
        assert isinstance(monkey, Monkey)
        return self.activity < monkey.activity

    def __mul__(self , monkey : Monkey) -> int:
        assert isinstance(monkey,Monkey)
        return self.activity*monkey.activity

class SimMixin:

    def _simulate(self , monkeys : list[Monkey], rounds : int):
        for idx in tqdm(range(rounds)):
            for monkey in monkeys.values():
                monkey.throw()

class MonkeyParser(Solution):

    def _monkey_construction(self , stress_relief : int = 3) -> None:
        instructions = [instructions.strip() for instructions in re.split("Monkey \d:(.*)" ,self.challenge_data) if len(instructions) > 0]

        ##constructing the monkeys!
        for num , monkey in enumerate(instructions):
            monkey_data = monkey.split("\n")
            items = [int(d.strip()) for d in monkey_data[0].split(":")[-1].split(",")]
            operate = eval(f"lambda old:" + monkey_data[1].split("=")[-1])
            div_criterion = int(re.split("(\d+)" , monkey_data[2])[-2])
            first_monkey = int(re.split("(\d+)" , monkey_data[3])[-2])
            second_monkey = int(re.split("(\d+)" , monkey_data[4])[-2])
            Monkey(**{"num" : num ,"items": items, "stress_relief": stress_relief, "operate":operate, "div_criterion":div_criterion, "throw_to":(first_monkey,second_monkey)})

class PartI(MonkeyParser,SimMixin):

    def solve(self):
        ##construct monkeys
        self._monkey_construction(stress_relief = 3)
        ##simulating monkey behaviour
        self._simulate(Monkey.monkeys , rounds = 20)
        return reduce(mul , sorted(Monkey.monkeys.values() , reverse = True)[:2])


class PartII(MonkeyParser,SimMixin):

   def solve(self):


    ##construct monkeys
    self._monkey_construction(stress_relief = 1)
    ##simulating monkey behavior
    self._simulate(Monkey.monkeys , rounds = 10000)

    return reduce(mul , sorted(Monkey.monkeys.values() , reverse = True)[:2])


if __name__ == "__main__":
    solution=PartI().solve()
    print(solution)
    solution=PartII().solve()
    print(solution)
