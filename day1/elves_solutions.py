from data_source import Solution

class PartI(Solution):

    def solve(self) -> int:
        """Part I SolutiooOOOonNNNNnn!"""
        return max(map(lambda s : sum(int(num) for num in s.split("\n")) , self.data.strip().split("\n"*2)))

class PartII(Solution):

    def solve(self) -> int:
        """Part II SolutiOOOnNnNNnN!"""
        return sum(sorted(map(lambda s : sum(int(num) for num in s.split("\n")) , self.data.strip().split("\n"*2)) , reverse = True)[:3])
