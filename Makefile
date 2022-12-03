clean:
	@echo "Invoked Cleaning Magic!"
	@find . -type d -name '*__pycache__' -exec rm -rf {} +
	@find . -type d -name '*.egg-info' -exec rm -rf {} +


##Boilerplate to kickstart your daily AoC challenges
day?=1
my_day:
	@mkdir pyaoc/day$(day) 2>/dev/null
	@touch pyaoc/day$(day)/__init__.py pyaoc/day$(day)/solution.py
	@echo "from pyaoc.data_source import Solution\n\nclass PartI(Solution):\n\n    def solve(self):\n        pass" >> pyaoc/day$(day)/solution.py
	@echo "\nclass PartII(Solution):\n\n   def solve(self):\n        pass" >> pyaoc/day$(day)/solution.py
	@echo "\n\n\nif __name__==\"__main__\":\n    solution=PartI().solve()\n    print(solution)" >> pyaoc/day$(day)/solution.py
