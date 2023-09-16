from collections import deque

def solution(n, m, numbers):
    answer = 0
    q = deque(numbers)

    numbers.sort()

    while True:
        if q[0] == numbers[-1]:
            answer += 1 #원하는 문서가 몇번째로 인쇄되는지
            q.popleft()
            numbers.pop()
            if m == 0:
                break
        else:
            q.append(q.popleft())
        m = len(q) - 1 if m==0 else m-1

    return answer

tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(solution(n, m, numbers))
