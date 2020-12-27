# Owned
__author__ = "Qaiser Abbas"
__copyright__ = "Copyright 2020, Artificial Intelligence lab-08"
__email__ = "qaiserabbas889@yahoo.com"
#===============================================================
# {code}
from sys import maxsize 
from itertools import permutations
V = 4

def travellingSalesmanProblem(graph, q): 
 
    vertex = [] 
    for i in range(V): 
        if i != q: 
            vertex.append(i) 
 
    min_path = maxsize 
    next_permutation=permutations(vertex)
    for i in next_permutation:
 
        current_pathweight = 0
 
        k = q 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][q] 

        min_path = min(min_path, current_pathweight) 
         
    return min_path 
 

if __name__ == "__main__": 
 
    graph = [[200, 210, 215, 220], [210, 200, 235, 225], 
            [215, 235, 200, 230], [220, 225, 230, 200]] 
    q = 3
    print(travellingSalesmanProblem(graph, q))
