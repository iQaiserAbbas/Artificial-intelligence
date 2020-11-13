__author__ = "Qaiser Abbas"
__copyright__ = "Copyright 2020, Artificial Intelligence lab-05"
__email__ = "qaiserabbas889@yahoo.com"

def dfs(graph,start,path=[]):
    stack=[start]
    while stack:
        v=stack.pop(0)
        if not v in path:
            path=path+[v]
            stack=graph[v]+stack
    return path
graph={ 'A':['B','C','D'],
        'B':['C','E'],
        'C':['E'],
        'D':['C','F'],
        'E':['A'],
        'F':['C'],
        'G':['D','F','H'],
        'H':['C']}
print('Depth First Search starting from A',dfs(graph,'A'))
print('\nDFS starting from B',dfs(graph,'B'))
print('\nDFS First Search starting from C',dfs(graph,'C'))
print('\nDFS First Search starting from D',dfs(graph,'D'))
print('\nDFS First Search starting from E',dfs(graph,'E'))
print('\nDFS First Search starting from F',dfs(graph,'F'))
print('\nDFS First Search starting from G',dfs(graph,'G'))
print('\nDFS First Search starting from H',dfs(graph,'H'))
