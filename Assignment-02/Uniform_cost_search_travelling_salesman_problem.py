# Owned
__author__ = "Qaiser Abbas"
__copyright__ = "Copyright 2020, Artificial Intelligence lab-06"
__email__ = "qaiserabbas889@yahoo.com"
#===============================================================
# {code}
import queue as Q
def search(graph, start, end):
    whileiterations = 0
    foriteration = 0
    if start not in graph:
        raise TypeError(str(start) + ' not found in graph !')
    if end not in graph:
        raise TypeError(str(end) + ' not found in graph !')
    queue = Q.PriorityQueue()
    queue.put((0, [start]))
    while not queue.empty():
        whileiterations = whileiterations+1
        node = queue.get()
        current = node[1][len(node[1]) - 1]
 
        
        cost = node[0]
        for neighbor in graph[current]:
            foriteration = foriteration+1
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))
def main():
    graph = {
    'A': {'B': 75, 'C': 118, 'D': 140, 'E': 131},
    'B': {'C': 120, 'D': 175, 'E': 110, 'A': 39},
    'C': {'D': 110, 'E': 241, 'A': 29, 'B': 180},
    'D': {'E': 130, 'A': 111, 'B': 99, 'C': 60},
    'E': {'A': 190, 'B': 151, 'C': 199, 'D': 180},
    }
      
main()
