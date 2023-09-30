from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, coord, visited):
    queue = deque([coord])

    visited[coord]=True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


# n: 정점(vertex)의 개수
# m: 간선(edge)의 개수
# v: 탐색 시작 정점
N, M, V = map(int, input().split())

# 인접 리스트 방식으로 graph 설정!
graph = [[] for _ in range(N+1)]
#0번째 인덱스를 두기 위해 (정점의 개수+1) 만큼의 인덱스 필요. 단, 0번째 인덱스는 실질적으로 사용되지 x

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


 for i in graph:
     i.sort()

visited = [False] * (N+1) #마찬가지로 0번째 index를 고려하여 (N + 1)
dfs(graph, V, visited)
visited = [False] * (N + 1)
print()
bfs(graph, V, visited)