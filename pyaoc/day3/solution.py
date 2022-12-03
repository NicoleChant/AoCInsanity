from pyaoc.data_source import Solution
from functools import reduce

class PartI(Solution):

    def solve(self):
        return sum(map(lambda row :sum(map(lambda x :ord(x) - 96 if ord(x) > 96 else ord(x) - 38,set(row[:len(row)//2]).intersection(row[len(row)//2:]))),self.challenge_data.split("\n")))

class PartII(Solution):

    def solve(self):
        return sum(map(lambda group:(lambda x : ord(x) - 96 if ord(x) > 96 else ord(x) - 38)(reduce(lambda acc , val : acc.intersection(val)  , group[1:] , set(group[0])).pop()) ,zip(*[iter(self.challenge_data.split("\n"))]*3)))
