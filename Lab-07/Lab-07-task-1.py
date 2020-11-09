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
        
        if end in node[1]:
            print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            break
        
        cost = node[0]
        for neighbor in graph[current]:
            foriteration = foriteration+1
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))
    print("Total while loop executed "+str(whileiterations)+" times")
    print("Total for loop executed "+str(foriteration)+" times")
def main():
    graph = {
    'Bahria University': {'Gulshan e Iqbal': 5, 'Bahadurabad': 8, 'Shah Faisal': 4},
    'Gulshan e Iqbal': {'Gulistan e johar': 71, 'Bahria University': 35},
    'Bahadurabad': {'Bahria University': 18, 'NIPA': 11},
    'Shah Faisal': {'Bahria University': 90, 'Gulistan e johar': 31, 'Malir': 99, 'Airport': 60},
    'Gulistan e johar': {'Gulshan e Iqbal': 71, 'Shah Faisal': 51},
    'NIPA': {'Bahadurabad': 11, 'DHA': 70},
    'Airport': {'Shah Faisal': 80, 'Lyari': 97, 'Nazimabad': 46},
    'DHA': {'NIPA': 70, 'Karachi University': 75},
    'Nazimabad': {'Karachi University': 120, 'Airport': 146, 'Lyari': 138},
    'Lyari': {'Airport': 97, 'Nazimabad': 138, 'Korangi': 101},
    'Malir': {'Shah Faisal': 99, 'Korangi': 211},
    'Karachi University': {'DHA': 75, 'Nazimabad': 120},
    'Korangi': {'Malir': 211, 'Lyari': 101, 'Saddar': 90},
    'Saddar': {'Korangi': 90}
    }
    search(graph, 'Bahria University', 'Malir')
    
main()