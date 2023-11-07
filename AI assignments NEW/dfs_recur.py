visited = set()  # Create a set to keep track of visited nodes

def dfs(node, graph):
    if node not in visited:
        print(node)  # Process the current node
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, graph)  # Recursively visit unvisited neighbors

# Input the graph from the user
graph = {}
print("Enter the graph as an adjacency list. Enter 'done' when finished.")
while True:
    node = input("Enter node (or 'done' to finish): ")
    if node == 'done':
        break
    neighbors = input(f"Enter neighbors for node {node} separated by spaces: ").split()
    graph[node] = neighbors

# Start DFS from an initial node (e.g., 'A')
initial_node = input("Enter the initial node to start DFS from: ")
dfs(initial_node, graph)
