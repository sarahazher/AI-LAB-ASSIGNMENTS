from collections import deque

def addnode(v, g):
    if v in g:
        print(v, "is present already")
    else:
        g[v] = []

def addedge(v1, v2, g):
    if v1 not in g:
        print(v1, "not present in graph")
    elif v2 not in g:
        print(v2, "not present in graph")
    else:
        g[v1].append(v2)
        g[v2].append(v1)

def dfs(n, vis, g):
    if n not in vis:
        print(n)
        vis.add(n)
        for i in g[n]:
            dfs(i, vis, g)

def bfs(queue, vis, g):
    if not queue:
        return
    n = queue.popleft()
    if n not in vis:
        print(n)
        vis.add(n)

    for neighbor in g[n]:
        if neighbor not in vis and neighbor not in queue:
            queue.append(neighbor)

    bfs(queue, vis, g)

vis = set()
g = {}

addnode("a", g)
addnode("b", g)
addnode("c", g)
addnode("d", g)
addnode("e", g)

addedge("a", "b", g)
addedge("b", "e", g)
addedge("a", "c", g)
addedge("a", "d", g)
addedge("b", "d", g)
addedge("c", "d", g)
addedge("e", "d", g)

print("DFS (Starting from vertex 'a'):")
dfs("a", vis, g)

print("\nBFS (Starting from vertex 'a'):")
bfs(deque(["a"]), set(), g)
