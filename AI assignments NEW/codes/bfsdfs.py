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
# This code is a Python program that allows a user to input a graph in the form of an adjacency list and
# then perform Breadth-First Search (BFS) and Depth-First Search (DFS) traversals starting from a user-specified node.
# Here's an explanation of how the code works:

# 1. Import Required Modules:
#    - `deque` is imported from the `collections` module to use it for implementing the queue data structure for BFS.

# 2. Define BFS and DFS Functions:
#    - `bfs(graph, start)`: This function takes a graph (represented as an adjacency list) and a starting 
# node as input. It performs a BFS traversal starting from the given node. It maintains a set called `visited` 
# to keep track of visited nodes, initializes a queue with the starting node, and adds the starting node to the set of 
# visited nodes. Then, it enters a loop that continues as long as there are nodes in the queue.
#      - Inside the loop, it dequeues a node from the front of the queue (FIFO order) and prints it. 
# his is the current node being visited.
#      - For each neighbor of the current node (obtained from the adjacency list), if the neighbor has not 
# been visited, it is enqueued into the queue, and its status is updated in the `visited` set.
#    - `dfs(graph, start)`: This function takes a graph and a starting node as input. It performs a 
# DFS traversal starting from the given node. It uses a stack to keep track of nodes and a set called 
# `visited` to mark visited nodes.
#      - The DFS process is similar to BFS, with some differences:
#        - It starts by pushing the starting node onto the stack.
#        - Inside the loop, it pops a node from the top of the stack (LIFO order), which is the current node.
#        - It prints the current node and marks it as visited.
#        - Unvisited neighbors of the current node are pushed onto the stack in reverse order to
# ensure that the leftmost unvisited neighbor is visited next.

# 3. Input the Graph:
#    - An empty dictionary called `graph` is created to represent the graph.
#    - The program enters a loop, asking the user for input regarding nodes and their neighbors. 
# The user can enter node names, followed by their neighbors separated by spaces.
#    - The loop continues until the user presses Enter without typing a node name (leaving the input 
#    field empty). This signals the end of graph input.
#    - The adjacency list of the graph is populated with user input data.

# 4. Start BFS and DFS Traversals:
#    - The program then prompts the user to enter the starting node for BFS and DFS traversals.
#    - The BFS traversal is initiated using the `bfs` function, starting from the specified node. 
# It prints the BFS traversal order.
#    - The user is then prompted to enter the starting node for DFS traversal, and the DFS traversal
#    is initiated using the `dfs` function, starting from the specified node. It prints the DFS traversal order.

# This code provides a way for users to input a graph, specify a starting node, and visualize 
# both BFS and DFS traversals in that graph. The adjacency list structure
#    makes it flexible to represent a variety of graphs.