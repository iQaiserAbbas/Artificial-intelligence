__author__ = "Qaiser Abbas"
__copyright__ = "Copyright 2020, Artificial Intelligence lab-05"
__email__ = "qaiserabbas889@yahoo.com"

def dfs(graph,start,path=[]):
    path=path+[start]
    for node in graph[start]:
        if not node in path:
            path=dfs(graph,node,path)
    return path
graph={ 'Q':['S','T','U'],
        'R':['S','T','V'],
        'S':['Q','R','W'],
        'T':['Q','R','U'],
        'V':['R'],
        'W':['S'],
        'U':['Q','T']}
print('\n Depth First Search starting from Q is given below:\n',dfs(graph,'U'))
