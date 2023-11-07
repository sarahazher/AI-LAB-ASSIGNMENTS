from collections import deque

def bfs(graph, start):
    visited = set()  # Keep track of visited nodes
    queue = deque([start])  # Use a queue for BFS
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

def dfs(graph, start):
    visited = set()  # Keep track of visited nodes
    stack = [start]  # Use a stack for DFS

    print("DFS Traversal:")
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            # Push unvisited neighbors onto the stack in reverse order.
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Input the graph as an adjacency list
graph = {}
while True:
    node = input("Enter a node (or press Enter to finish): ")
    if not node:
        break
    neighbors = input(f"Enter neighbors for node {node} separated by spaces: ").split()
    graph[node] = neighbors

# Accept user input for the starting node
start_node = input("Enter the starting node: ")

# Start BFS and DFS from the user-provided starting node
print("BFS Traversal:")
bfs(graph, start_node)

dfs_start_node = input("Enter the starting node for DFS: ")
print("DFS Traversal:")
dfs(graph, dfs_start_node)
