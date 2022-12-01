import requests
import os
from dotenv import load_dotenv
from termcolor import colored , cprint
from abc import abstractmethod , ABC
import argparse
load_dotenv()

class Solution(ABC):

    def __init__(self) -> None:
        """Just a helper constructor loading the data"""

        if not os.path.isfile("challenge.txt"):
            response = requests.request("GET",
                            os.getenv('url') , 
                            headers = {'Cookie':os.getenv('cookie')} )
            if response.status_code == 200:
                with open("challenge.txt" , mode = "w+") as f:
                    f.write(response.text)
                print("Data succesfully stored!")
        
        ##read data
        self.data = None
        with open("challenge.txt" , mode = "r+") as f:
            self.data = f.read()
        print("Data succesfully read!")
    
    @abstractmethod
    def solve(self):
        ...

class PartI(Solution):

    def solve(self) -> int:
        """Part I SolutiooOOOonNNNNnn!"""
        return max(map(lambda s : sum(int(num) for num in s.split("\n")) , self.data.strip().split("\n"*2)))

class PartII(Solution):

    def solve(self) -> int:
        """Part II SolutiOOOnNnNNnN!"""
        return sum(sorted(map(lambda s : sum(int(num) for num in s.split("\n")) , self.data.strip().split("\n"*2)) , reverse = True)[:3])


solutions = {1 : PartI , 2 : PartII }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "AoC Solutions Day I")
    parser.add_argument("--part" , type=int , choices=[1,2] , default=1)
    args = parser.parse_args()
    solution = solutions.get(args.part)().solve()
    print(solution)
    if args.part == 1:
        cprint(f"The elf 🧝 with maximum cookie cargo carries {max_elf_cargo} calories! 🍪" , "red" , attrs = ["bold",'reverse', 'blink'])
