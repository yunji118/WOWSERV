def solution(n, score):
    answer = 0
    dp = [0] * 301 #계단 수는 3개 이상 300개 이하로 가정 & 점화식 편의상 인덱스 1부터 사용

    dp[1] = score[1] #1번째 계단 sum 최댓값: 1번쨰 계단
    dp[2] = score[1] + score[2] #2번째 계단은 sum 최댓값: 1번째 + 2번쨰 계단

    for i in range(3, n+1):
        #dp[i-3]: score[i-3]까지의 max
        #dp[i-2]: score[i-2]까지의 max
        #score[i] -> 마지막 계단. 무조건 밟음.

        #score[i-2]를 거치지 않는 경우-> dp[i-3]+score[i-1]+score[i]
        #score[i-2]를 거치는 경우-> dp[i-2]+score[i] => because 연속 3개의 칸 안됨!
        #1칸 전에서 온 경우(3칸 전 최댓값에서 + 2칸 이동한 1칸 전 값), 2칸 전에서 온 경우(2칸 전의 최댓값) 중 최댓값 + 현재 계단 값
        dp[i] = max(dp[i-3] + score[i -1], dp[i-2]) + score[i]

    answer = dp[n]
    return answer

if __name__ == "__main__":
    n = int(input())
    score = [0] * 301

    for i in range(1, n+1):
        score[i] = int(input())

    answer = solution(n, score)
    print(answer)