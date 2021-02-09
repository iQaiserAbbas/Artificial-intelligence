__author__ = "Qaiser Abbas"
__copyright__ = "Copyright 2020, Artificial Intelligence Assignment-02"
__email__ = "qaiserabbas889@yahoo.com"

edges = []
print("Enter the distance of All cities from City A:")
edges_cityA = []
edges_cityB = []
edges_cityC = []
edges_cityD = []
edges_cityE = []
cost = int(input())
edges_cityA.append(0)
edges_cityA.append(cost)
cost = int(input())
edges_cityA.append(cost)
cost = int(input())
edges_cityA.append(cost)
cost = int(input())
edges_cityA.append(cost)
print("Enter the distances of All cities from city B")
cost = int(input())
edges_cityB.append(cost)
edges_cityB.append(0)
cost = int(input())
edges_cityB.append(cost)
cost = int(input())
edges_cityB.append(cost)
cost = int(input())
edges_cityB.append(cost)
print("Enter the distance of All cities from city C")
cost = int(input())
edges_cityC.append(cost)
cost = int(input())
edges_cityC.append(cost)
edges_cityC.append(0)
cost = int(input())
edges_cityC.append(cost)
cost = int(input())
edges_cityC.append(cost)
print("Enter the distance of All cities from city D")
cost = int(input())
edges_cityD.append(cost)
cost = int(input())
edges_cityD.append(cost)
cost = int(input())
edges_cityD.append(cost)
edges_cityD.append(0)
cost = int(input())
edges_cityD.append(cost)

print("Enter the distance of All cities from city E")
cost = int(input())
edges_cityE.append(cost)
cost = int(input())
edges_cityE.append(cost)
cost = int(input())
edges_cityE.append(cost)
cost = int(input())
edges_cityE.append(cost)
edges_cityE.append(0)

edges.append(edges_cityA)
edges.append(edges_cityB)
edges.append(edges_cityC)
edges.append(edges_cityD)
edges.append(edges_cityE)


def TSP_bfs(edges):
    q = []
    path = []
    visited = [False] * 6
    p = [0]
    q.append((0, 0, visited, p))
    while len(q) != 0:
        cnt = 0
        curr = q.pop(0)
        curr[2][curr[0]] = True
        for i in range(5):
            if curr[2][i] == False:
                cnt += 1
        if cnt == 0:
            P = curr[3]
            P.append(0)
            path.append((curr[1] + edges[curr[0]][0], P))
        for i in range(5):
            if curr[2][i] == False:
                tmp = [False] * 6
                for j in range(5):
                    tmp[j] = curr[2][j]
                P = []
                for j in range(len(curr[3])):
                    P.append(curr[3][j])
                P.append(i)
                q.append((i, curr[1] + edges[curr[0]][i], tmp, P))

    mini = 1000
    P = []
    for i in range(len(path)):
        if mini > path[i][0]:
            mini = path[i][0]
            P = path[i][1]
        return mini, P
print('******BFS Solution******')
print(TSP_bfs(edges))



def TSP_dfs(node, edges, visited, cost, path):
    cnt = 0
    path.append(node)
    visited[node] = True
    for i in range(5):
        if visited[i] == False:
            cnt += 1
    if cnt == 0:
        path.append(0)
        return (cost + edges[node][0]), path
    mini = 10000
    A = []
    for i in range(5):
        if visited[i] == False:
            tmp = [False]*6
            for j in range(5):
                tmp[j] = visited[j]
            P = []
            for j in range(len(path)):
                P.append(path[j])
            t, l = TSP_dfs(i, edges, tmp, cost + edges[node][i], P)
            if mini > t:
                mini = t
                A = l
    return mini, A

visited = [False]*6
path = []
print('******DFS Solution******')
print(TSP_dfs(0, edges, visited, 0, path))