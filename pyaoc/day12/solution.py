from pyaoc.data_source import Solution

class PartI(Solution):

    def find_starting_position(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == "S":
                    return i , j

    def print_maze(self):
        for row in self.maze:
            for data in row:
                print(data , end = " ")
            print()

    def is_valid(self , cur_pos , move):
        i , j = cur_pos
        cur_elevation = self.maze[i][j]
        if move == "^":
            i += 1
        elif move == "v":
            i -= 1
        elif move == ">":
            j += 1
        elif move == "<":
            j -= 1

        if 0 <= i < len(self.maze) and 0 <= j < len(self.maze[0]):
            return True , i , j
        return False , i , j

    def backtrack_path(self , parents , start , last_node):
        path = [last_node]
        while path[-1]!=start:
            path.append(parents[path[-1]])
        return path[::-1]

    def save_maze(self):
        with open("maze.txt","w+") as f:
            f.write("\n".join("".join(row) for row in self.maze))

    def solve(self):
        self.maze = [list(row) for row in self.challenge_data.splitlines()]
        #self.print_maze()
        parents = {}
        path = None
        start = self.find_starting_position()
        queue = [start]
        print(f"Start = {start}")

        while len(queue) > 0:
            cur_pos = queue.pop(0)
            if self.maze[cur_pos[0]][cur_pos[1]] == "E":
                path = cur_pos
                break

            for move in [">","<","^","v"]:
                # what am i doing? ...
                validation , next_i , next_j = self.is_valid(cur_pos , move)
                if validation:
                    next_elevation = self.maze[next_i][next_j]
                    cur_elevation = self.maze[cur_pos[0]][cur_pos[1]]

                    ##stupid... i got 0 nodes.. need to change S --> elevation a
                    if cur_elevation == "S":
                        cur_elevation = "a"

                    #check elevation ..... YAY! pro climber
                    ##skip if you dont have the right elevation!!!
                    if ord(cur_elevation) + 1 < ord(next_elevation):
                        continue

                    next_pos = next_i , next_j
                    if next_pos not in parents:
                        #i dont need that i think lol
                        parents[next_pos] = cur_pos
                        queue.append(next_pos)

        full_path = self.backtrack_path(parents , start , path)
        print(full_path)

        ##visualization of the path

        for pos in parents:
            self.maze[pos[0]][pos[1]] = "#"

        for pos in full_path:
            self.maze[pos[0]][pos[1]] = "*"

        #self.print_maze()
        ##save the modified maze
        self.save_maze()

        ##substract one at the end --->!!!!!
        return -1 if not path else len(full_path)-1
        #return -1 if not path else cur_pos


class PartII(Solution):

   def solve(self):
        pass



if __name__=="__main__":
    solution=PartI().solve()
    print(solution)
