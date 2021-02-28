import osmnx as ox
import heapq as hq

def dijkstra_path(G, source, dest):
    distances = {} # final distances
    boundary = []
    predecessors = {}

    for node in G.nodes:
        distances[node] = float('inf')
    distances[source] = 0
    hq.heappush(boundary, (0, source))
    predecessors[source] = []
    count=0
    while boundary:
        (dist, u) = hq.heappop(boundary)

        if u == dest:
            break
        
        if dist <= distances[u]:
            for v, e in G.succ[u].items():
                alt_path = distances[u] + G[u][v][0]['length']
                if alt_path <= distances[v]:
                    hq.heappush(boundary, (alt_path, v))
                    distances[v] = alt_path
                    predecessors[v] = predecessors[u][:]
                    predecessors[v].append(u)

    return predecessors[dest]
                