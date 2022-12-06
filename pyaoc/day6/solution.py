from pyaoc.data_source import Solution

class PartI(Solution):

    def solve(self):
        return next(filter(lambda i : len(set(self.challenge_data[i:i+4]))==4 , range(len(self.challenge_data)-3))) + 4

class PartII(Solution):

   def solve(self):
        return next(filter(lambda i : len(set(self.challenge_data[i:i+14]))==14 , range(len(self.challenge_data)-14+1))) + 14



if __name__=="__main__":
    solution=PartII().solve()
    print(solution)
