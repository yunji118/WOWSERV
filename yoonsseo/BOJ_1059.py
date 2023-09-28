L = int(input())
S = list(map(int, input().split()))
n = int(input())

S.sort()

if n in S :
    print(0)
else :
    start = end = 0
    for s in S :
        if s < n : # n보다 작은 수 중 가장 큰 수
            start = s
        elif n < s and end == 0 : # n보다 큰 수 중 가장 작은 수!
            end = s

    start += 1
    end -= 1

    total = (n-start) * (end-n+1) + (end - n)
    print(total)