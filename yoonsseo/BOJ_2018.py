N = int(input())
start = end = 1
sum = cnt = 0
while start <= N :
    if sum == N :
        cnt += 1
        sum -= start
        start += 1
    elif sum > N :
        sum -= start
        start += 1
    else : # sum < N
        sum += end
        end += 1
print(cnt)
