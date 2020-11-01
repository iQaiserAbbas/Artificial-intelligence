__author__ = "Qaiser Abbas"
__copyright__ = "Copyright 2020, Artificial Intelligence lab-04"
__email__ = "qaiserabbas889@yahoo.com"

def BFS(graph, start, path=[]):
    q = [start]
    while q:
        v = q.pop(0)
        if not v in path:
            path = path+[v]
            q = q+graph[v]
    return path
graph = {
    'A':['B','C','D'],
    'B':['A','E'],
    'C':['A','F','D'],
    'E':['B'],
    'F':['C'],
    'D':['A','C']
}
print("Breadth First Search", BFS(graph,'A'))
