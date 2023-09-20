N = int(input())
number = [input() for _ in range (N)]

k = 1
# set의 길이가 N과 같으면 겹치는 게 없다는 뜻
for k in range (1, 101) :
    if len(set(map(lambda x : x[-k:], number))) == N :
        print(k)
        break