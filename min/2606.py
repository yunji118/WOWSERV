ans = 0
def DFS(virus):
    global ans
    visited[virus] = True

    for i in network[virus]:
        if (visited[i]== False):
            DFS(i)
            ans += 1

def BFS(virus):
    global ans
    visited[virus] = True
    queue = [virus]
    while queue:
        for i in network[queue.pop()]:
            if (visited[i] == False):
                visited[i] = True
                queue.insert(0, i)
                ans += 1


N= int(input())
link = int(input())

network = [[]*(N+1) for _ in range(N+1)]

for i in range(link):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

visited = [0] * (N+1)
BFS(1)
print(ans)