from pyaoc.data_source import Solution

class PartI(Solution):

    def solve(self):
        data = self.challenge_data.splitlines()
        visibility = [[False for _ in range(len(data[0]))] for _ in range(len(data))]
        total = 0
        for i in range(1,len(data)-1):
            for j in range(1,len(data[0])-1):
                tree = data[i][j]
                visibility[i][j] = all(tree>data[i][k] for k in range(0,j)) \
                                or all(tree>data[i][k] for k in range(j+1,len(data[0]))) \
                                or all(tree>data[k][j] for k in range(0,i)) \
                                or all(tree>data[k][j] for k in range(i+1,len(data)))
                total += int(visibility[i][j])
        return total + 2*len(data) + 2*len(data[0]) - 4


class PartII(Solution):

   def solve(self):
        data = self.challenge_data.splitlines()
        max_scentic = 0
        for i in range(1,len(data)-1):
            for j in range(1,len(data[0])-1):
                tree = data[i][j]

                scentic_score_up = 0
                for k in range(j-1,-1,-1):
                    scentic_score_up += 1
                    if tree<=data[i][k]:
                        break

                scentic_score_down = 0
                for k in range(j+1,len(data[0]),1):
                    scentic_score_down += 1
                    if tree<=data[i][k]:
                        break

                scentic_score_left = 0
                for k in range(i-1,-1,-1):
                    scentic_score_left += 1
                    if tree <= data[k][j]:
                        break

                scentic_score_right = 0
                for k in range(i+1,len(data),+1):
                    scentic_score_right += 1
                    if tree <= data[k][j]:
                        break

                scentic_score = scentic_score_up*scentic_score_right*scentic_score_left*scentic_score_down
                if scentic_score > max_scentic:
                    max_scentic = scentic_score
        return max_scentic


if __name__=="__main__":
    solution=PartII().solve()
    print(solution)
