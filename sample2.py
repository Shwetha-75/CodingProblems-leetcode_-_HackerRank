def findCheapestCost(n, graph, src, dst, k):
 
    # if the destination cannot be reached
    if dst > n:
      return -1;
    # Increase k by 1 Because on reaching
    # destination, k becomes k+1
    k = k + 1
 
    # Making Adjacency List
    adj = [[] for _ in range(n)]
 
    # U->{v, wt}
    for it in graph:
        adj[it[0]].append([it[1], it[2]])
    print(adj)
n = 6
graph = [
            [0, 1, 10],
            [1, 2, 20],
            [2, 5, 30],
            [1, 3, 10],
            [3, 4, 10],
            [4, 5, 10]]
 
src = 0
dst = 5
k = 2
findCheapestCost(n, graph, src, dst, k)