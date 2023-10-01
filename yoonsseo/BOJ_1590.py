N, T = map(int, input().split())
result = []

for _ in range(N):
    S, I, C = map(int, input().split())
    time = [S + (I * c) for c in range(C)]
    if time[-1] < T:
        continue

    # 이분탐색
    start = 0
    end = C - 1
    answer = 0
    while (start <= end):
        mid = (start + end) // 2
        if time[mid] >= T:
            answer = mid
            end = mid - 1
        else : #time[mid] < T
            start = mid + 1

    result.append(time[answer] - T)

if len(result) == 0 :
    print(-1)
else :
    print(min(result))