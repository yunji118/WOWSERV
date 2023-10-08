zero = [0] * 41
zero[0] = 1
zero[2] = 1

one = [0] * 41
one[1] = 1
one[2] = 1

for i in range (3, 41) :
    zero[i] = zero[i-2] + zero[i-1]
    one[i] = one[i-2] + one[i-1]

T = int(input())
for _ in range (T) :
    N = int(input())
    print("%d %d" %(zero[N], one[N]))