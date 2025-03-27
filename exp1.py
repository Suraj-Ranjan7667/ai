from collections import deque  
def bfs(graph, start):
    visited = set()  
    queue = deque([start])  

    while queue:  
        node = queue.popleft()  
        if node not in visited: 
            print(node, end=" ")  
            visited.add(node) 
            queue.extend(graph[node])  

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H'],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}

print("BFS Traversal:")
bfs(graph, 'A')