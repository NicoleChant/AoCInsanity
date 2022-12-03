from pyaoc.data_source import Solution

class PartI(Solution):

    def solve(self):
        return sum(map(lambda row : sum(map(lambda x :ord(x) - 96 if ord(x) > 96 else ord(x) - 38
                , set(row[:len(row)//2]).intersection(row[len(row)//2:]))),
                self.challenge_data.strip().split("\n")))

class PartII(Solution):

   def solve(self):
        idx = 0
        total = 0
        temp = set()
        for d in self.challenge_data.strip().split("\n"):
            if idx%3==0:
                temp = set(d)
            else:
                temp = temp.intersection(d)

            if len(temp) == 1:
                x = list(set(temp))[0]
                total += ord(x) - 96 if ord(x) > 96 else ord(x) - 38
            idx += 1
        return total



if __name__ == "__main__":
    solution=PartII().solve()
    print(solution)
