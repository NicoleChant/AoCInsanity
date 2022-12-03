from pyaoc.data_source import Solution

class PartI(Solution):

    def solve(self):
        rewards = {"X":1,"A":1,"Y":2,"B":2,"C":3,"Z":3}
        return sum(map(lambda d: rewards[d.split(" ")[1]] \
            + (lambda x ,y: 6 if {"Y":"A","X":"C","Z":"B"}[y]==x \
               else (3 if rewards[x] is rewards[y] else 0))(*d.split(" ")) if d else 0
            , self.challenge_data.strip().split("\n")))


class PartII(Solution):

    def solve(self):
        rewards = {"X":0,"A":1,"Y":3,"B":2,"C":3,"Z":6}
        winners = {"A":"C","B":"A","C":"B"}
        return sum(map(lambda d: rewards[d.split(" ")[1]] \
            + (lambda x ,y: rewards[winners[x]] if y == "X" \
               else (rewards[x] if y == "Y" \
               else rewards[winners[winners[x]]]))(*d.split(" ")) if d else 0
            , self.challenge_data.strip().split("\n")))


if __name__ == "__main__":
    s = PartII().solve()
    print(s)
