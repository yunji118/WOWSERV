N, M = map(int, input().split())
if N == 0 :
  print(0)
else :
  weight = list(map(int, input().split()))

cnt = 1
sum = 0
for i in range (N) :
    sum += weight[i]
    if sum > M :
        cnt += 1
        sum = weight[i]
print(cnt)