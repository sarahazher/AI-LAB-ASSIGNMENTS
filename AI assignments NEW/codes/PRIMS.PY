import sys

class Graph():
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printMST(self, parent):
		print("Edge \tWeight")
		for i in range(1, self.V):
			print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

	def minKey(self, key, mstSet):
		min = sys.maxsize
		for v in range(self.V):
			if key[v] < min and mstSet[v] == False:
				min = key[v]
				min_index = v
		return min_index

	def primMST(self):
		key = [sys.maxsize] * self.V
		parent = [None] * self.V 
		key[0] = 0
		mstSet = [False] * self.V
		parent[0] = -1 
		for cout in range(self.V):
			u = self.minKey(key, mstSet)
			mstSet[u] = True
			for v in range(self.V):
				if self.graph[u][v] > 0 and mstSet[v] == False \
				and key[v] > self.graph[u][v]:
					key[v] = self.graph[u][v]
					parent[v] = u

		self.printMST(parent)

if __name__ == '__main__':
	g = Graph(5)
	g.graph = [[0, 2, 0, 6, 0],
			[2, 0, 3, 8, 5],
			[0, 3, 0, 0, 7],
			[6, 8, 0, 0, 9],
			[0, 5, 7, 9, 0]]

	g.primMST()

# This code demonstrates the Prim's algorithm for finding the Minimum Spanning Tree (MST) of a weighted undirected graph.
# The MST of a graph is a subset of the edges that form a tree and includes all vertices while minimizing the total edge weight. 
# Here's an explanation of how this code works:

# 1. `Graph` Class:
#    - The `Graph` class is defined to represent a graph.
#    - The constructor `__init__` takes the number of vertices (`vertices`) and initializes the graph as an
# adjacency matrix with all edge weights set to 0.

# 2. `printMST` Method:
#    - The `printMST` method is responsible for printing the Minimum Spanning Tree (MST) of the graph. It takes a 
# `parent` array as an argument, where `parent[i]` stores the parent of vertex `i` in the MST.
#    - It iterates through the vertices, starting from the second vertex (index 1), and prints the edges and their
# weights that make up the MST.

# 3. `minKey` Method:
#    - The `minKey` method finds the vertex with the minimum key value that is not included in the MST yet.
# 	It takes two arguments: `key`, an array of key values, and `mstSet`, a boolean array to keep track of the 
# 	vertices that are already included in the MST.
#    - It finds the vertex with the minimum key value (`key[v]`) among the vertices that are not yet included in 
# the MST (`mstSet[v] == False`).

# 4. `primMST` Method:
#    - The `primMST` method finds the MST of the graph using Prim's algorithm.
#    - It initializes three arrays: `key`, `parent`, and `mstSet`. The `key` array stores the key values (weights)
# of vertices, the `parent` array keeps track of the parent vertices in the MST, and the `mstSet` array is used
# to mark vertices that are included in the MST.
#    - The algorithm starts with vertex 0 as the root. It initializes the key value for all vertices to a large value
# 	(infinity), sets the parent of the root to -1, and marks the root as part of the MST.
#    - The main loop runs for each vertex (except the root) to build the MST. In each iteration, it finds the vertex 
# with the minimum key value among the vertices that are not in the MST.
#    - It then adds the selected vertex to the MST, updates the key values of its neighbors if they are smaller, and 
#    sets the selected vertex as their parent.
#    - After the loop, the method calls `printMST` to print the edges and their weights of the MST.

# 5. `if __name__ == '__main__'` Block:
#    - In the `if __name__ == '__main__'` block, an instance of the `Graph` class is created with 5 vertices.
#    - The adjacency matrix of the graph is provided with weight values, representing the weights of edges between 
# vertices. This data defines the input graph for the MST problem.

# 6. Running `primMST`:
#    - Finally, the `primMST` method is called to find and print the Minimum Spanning Tree of the graph, starting 
# from vertex 0 as the root.

# In summary, this code implements Prim's algorithm for finding the Minimum Spanning Tree of a given weighted graph 
# and demonstrates its use with a sample graph. The Minimum Spanning Tree represents a subset of edges that connects 
# all vertices with the minimum total weight.