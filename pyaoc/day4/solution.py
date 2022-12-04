from pyaoc.data_source import Solution

class PartI(Solution):

    def solve(self) -> int:
        return sum(map(lambda row : (lambda elf1 , elf2 : (lambda x , y , a , b : (int(a) <= int(x) and int(y) <= int(b)) or (int(x) <= int(a) and int(b) <= int(y) ) ) (*elf1.split("-"),*elf2.split("-")))(*row.split(",")) , self.challenge_data.split("\n")))


class PartII(Solution):

   def solve(self) -> int:
        return sum(map(lambda row : (lambda elf1 , elf2 : (lambda x , y , a , b : not (int(b) < int(x) or int(y) < int(a)))(*elf1.split("-"),*elf2.split("-")))(*row.split(",")) , self.challenge_data.split("\n")))


if __name__=="__main__":
    solution=PartII().solve()
    print(solution)
