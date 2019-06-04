#_*_coding:utf-8_*_
#单源最短路径问题

MAX_value = 999999

def dijkstra(graph, s):  #s是源点，d(s) = 0
    if graph is None:    # 判断图是否为空，如果为空直接退出
        return None
    dist = [MAX_value,]*len(graph)
    dist[s] = 0
    S = []
    Q = [i for i in range(len(graph))]
    dist_init = [i for i in graph[s]]
    while Q:
        u_dist = min([d for v, d in enumerate(dist_init) if v in Q])
        u = dist_init.index(u_dist)
        S.append(u)
        Q.remove(u)
 
        for v, d in enumerate(graph[u]):
            if 0 < d < MAX_value:
                if dist[v] > dist[u]+d:
                    dist[v] = dist[u]+d
                    dist_init[v] = dist[v]
                    print(dist[v])
    return dist    #到每一个点的最短路径距离
 
 
if __name__ == '__main__':
    graph_list = [  [0, 9, MAX_value, MAX_value, MAX_value, 14, 15, MAX_value],
                    [9, 0, 24, MAX_value, MAX_value, MAX_value,MAX_value,MAX_value],
                    [MAX_value, 24, 0, 6, 2, 18,MAX_value,19],
                    [MAX_value, MAX_value, 6, 0, 11,MAX_value,MAX_value, 6],
                    [MAX_value,MAX_value, 2, 11, 0, 30,20, 16],
                    [14,MAX_value,18,MAX_value,30,0,5,MAX_value],
                    [15,MAX_value,MAX_value,MAX_value,20,5,0,44],
                    [MAX_value,MAX_value,19,6,16,MAX_value,44,0]]
 
    distance = dijkstra(graph_list, 0)
    print(distance)  