dp = [[0] * 31 for _ in range(31)]
for i in range(31):
    dp[i][i] = 1
    dp[1][i] = i
    for j in range(i+1, 31):
        dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(dp[N][M])