from pyaoc.data_source import Solution

class PartI(Solution):

    def solve(self):
        return sum(map(lambda row : sum(map(lambda x :ord(x) - 96 if ord(x) > 96 else ord(x) - 38
                , set(row[:len(row)//2]).intersection(row[len(row)//2:]))),
                self.challenge_data.strip().split("\n")))

class PartII(Solution):

   def solve(self):
        pass



if __name__=="__main__":
    solution=PartI().solve()
    print(solution)
