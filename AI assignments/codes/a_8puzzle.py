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

# Example usage:
initial_state = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

solution = a_star_search(initial_state, goal_state)
if solution:
    for i, node in enumerate(solution):
        if node.move != "Initial":
            print(f"Step {i}: {node.move}")
else:
    print("No solution found")
