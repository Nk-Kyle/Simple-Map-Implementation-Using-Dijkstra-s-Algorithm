from cmath import inf
from heapq import *


mat = []
# Read input
with open('input/test.txt', 'r') as f:
    lines = f.readlines()
    for i in range (len(lines)):
        mat += [list(map(int, lines[i].split()))]

def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)

def djikstra(mat, source, target):
    dist = [inf for i in range(len(mat))]
    prev = [-1 for i in range(len(mat))]
    done = [False for i in range(len(mat))]
    dist[source] = 0
    done[source] = True
    q = []
    for i in range(len(mat)):
        heappush(q, (dist[i], i))
    
    while q:
        u = heappop(q)[1]
        for v in range(len(mat)):
            if (mat[u][v] != -1 and done[v] == False):
                alt = dist[u] + mat[u][v]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heappush(q, (dist[v], v))
        done[u] = True
    print(dist)
    route = []
    get_route(prev, target, route)
    print(f'Path ({source} —> {i}): Minimum cost = {dist[target]}, Route = {route}')