from queue import PriorityQueue
import copy

class PuzzleNode:
    def __init__(self, state, parent=None, move="Initial", depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth

    def __lt__(self, other):
        return self.depth + self.h() < other.depth + other.h()

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def is_goal(self, goal_state):
        return self.state == goal_state

    def h(self):
        # Manhattan distance heuristic
        total_distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    continue
                target_row, target_col = divmod(self.state[i][j] - 1, 3)
                total_distance += abs(i - target_row) + abs(j - target_col)
        return total_distance

    def get_neighbors(self):
        neighbors = []
        i, j = next((i, j) for i, row in enumerate(self.state) for j, val in enumerate(row) if val == 0)
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < 3 and 0 <= y < 3:
                new_state = copy.deepcopy(self.state)
                new_state[i][j], new_state[x][y] = new_state[x][y], new_state[i][j]
                neighbors.append(PuzzleNode(new_state, self, new_state[i][j], self.depth + 1))
        return neighbors

def a_star_search(initial_state, goal_state):
    initial_node = PuzzleNode(initial_state)
    goal_node = PuzzleNode(goal_state)
    if initial_node.is_goal(goal_state):
        return [initial_node]

    frontier = PriorityQueue()
    frontier.put(initial_node)
    explored = set()

    while not frontier.empty():
        current_node = frontier.get()
        explored.add(current_node)

        for neighbor in current_node.get_neighbors():
            if neighbor.is_goal(goal_state):
                # Reconstruct the path from the goal node to the initial node
                path = [neighbor]
                while neighbor.parent:
                    path.append(neighbor.parent)
                    neighbor = neighbor.parent
                return list(reversed(path))
            if neighbor not in explored:
                frontier.put(neighbor)

    return None

# Input initial state from the user
print("Enter the initial state (3x3 matrix, use space to separate values):")
initial_state = []
for i in range(3):
    row = list(map(int, input().split()))
    initial_state.append(row)

# Input goal state from the user
print("Enter the goal state (3x3 matrix, use space to separate values):")
goal_state = []
for i in range(3):
    row = list(map(int, input().split()))
    goal_state.append(row)
solution = a_star_search(initial_state, goal_state)
if solution:
    for i, node in enumerate(solution):
        if node.move != "Initial":
            print(f"Step {i}: {node.move}")
else:
    print("No solution found")


# This code implements the A* algorithm to solve the 8-puzzle problem. The 8-puzzle is a sliding puzzle that 
# consists of an initial state with a 3x3 grid containing numbers from 1 to 8 (representing tiles) and one empty space. 
# he goal is to reach a target state (another 3x3 grid) by moving the tiles into the empty space one at a time, with the
# fewest possible moves.

# Here's how the code works:

# 1. `PuzzleNode` class: This class represents a node in the search tree. Each node stores the 
# current state of the puzzle, a reference to its parent node, the move made to reach this state, and
# the depth of the node in the search tree. It also provides methods for comparing nodes and computing the 
# Manhattan distance heuristic.

# 2. `a_star_search` function: This function takes the initial state and goal state of the puzzle as input.
# It performs the A* search to find the optimal path from the initial state to the goal state.

#    - It starts by creating an `initial_node` and a `goal_node` using the provided initial and goal states.
#    - It checks if the `initial_node` is already in the goal state. If it is, the solution is found, and it
# returns a list containing the `initial_node`.
#    - It uses a `frontier` data structure (implemented as a priority queue) to store nodes yet to be explored
# and an `explored` set to store nodes that have been explored.
#    - The A* search proceeds by iteratively selecting nodes from the `frontier` based on their 
# estimated cost (heuristic) plus the depth in the search tree.
#    - For each selected node, it generates its neighboring states by making valid moves (up, 
#  down, left, or right). These neighboring states are represented as new `PuzzleNode` instances.
#    - If any of the neighboring states is the goal state, the code reconstructs the path from
# the goal node back to the initial node and returns it.
#    - Otherwise, it adds the neighboring states to the `frontier` for further exploration, 
# provided they are not in the `explored` set.

# 3. User Input:
#    - The code prompts the user to enter the initial state of the puzzle and the goal state, both as 3x3 matrices.
#    - The input states are stored as lists of lists, representing the grid.

# 4. Output:
#    - If a solution is found, it prints the steps needed to reach the goal state from the initial state, 
# indicating the moves made at each step.
#    - If no solution is found, it prints "No solution found."

# The code utilizes the A* algorithm, which combines Dijkstra's algorithm's breadth-first search with a 
# heuristic (in this case, the Manhattan distance) to efficiently 
# find the optimal solution to the 8-puzzle problem.