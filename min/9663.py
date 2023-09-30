import sys

n = int(sys.stdin.readline())
answer = 0

def check(x):
    for i in range(x):
        if visited[x]==visited[i] or abs(visited[x]-visited[i]) == abs(x-i):
            return False
    return True


def queen(x, n):
    global answer
    if x == n:
        answer += 1
    else:
        for i in range(n):
            visited[x] = i
            if check(x):
                queen(x + 1, n)


visited = [0] * n
queen(0, n)
print(answer)