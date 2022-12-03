from pyaoc.data_source import Solution

class PartI(Solution):

    def solve(self) -> int:
        """Part I SolutiooOOOonNNNNnn!"""
        return max(map(lambda s : sum(int(num) for num in s.split("\n")) , self.challenge_data.strip().split("\n"*2)))

class PartII(Solution):

    def solve(self) -> int:
        """Part II SolutiOOOnNnNNnN!"""
        return sum(sorted(map(lambda s : sum(int(num) for num in s.split("\n")) , self.challenge_data.strip().split("\n"*2)) , reverse = True)[:3])

if __name__ == "__main__":
    solution = PartI(day=1).solve()
    print(solution)
