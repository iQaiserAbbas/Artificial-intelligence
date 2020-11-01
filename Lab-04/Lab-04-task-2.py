__author__ = "Qaiser Abbas"
__copyright__ = "Copyright 2020, Artificial Intelligence lab-04"
__email__ = "qaiserabbas889@yahoo.com"

def part_short(graph,start,goal):
    explored=[]
    q=[start]
    if start==goal:
        return "start=goal"
    while q:
        path=q.pop(0)
        node=path[-1]
        neighbour=graph[node]
        for neighbour in neighbour:
            newpath=list(path)
            newpath.append(neighbour)
            q.append(newpath)
            if neighbour==goal:
                return newpath
        explored.append(node)
    return "sorry! connecting path does not exist"
graph={ 'A':['C','D','G'],
        'B':['C','D','E'],
        'C':['A','B','F'],
        'D':['A','B','G'],
        'E':['B', 'D'],
        'F':['C', 'B'],
        'G':['A','D']}
print('Shortest Path from G to E (using BFS) is given below:\n\n\t',part_short(graph,'G','E'))
