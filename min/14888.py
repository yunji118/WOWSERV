INF = 1000000000

def calculate(mode, x, y):
    if mode == 0: # '+' 연산
        return x + y
    elif mode == 1: # '-' 연산
        return x - y
    elif mode == 2: # '*' 연산
        return x * y
    elif mode == 3: # '/' 연산
        return int(x / y)

def backtracking(value, index, n, operand, operator_cnt, ans): #초기값: 첫번째 피연산자값, 1, 피연산자 개수, 피연산자 값 리스트, 연산자 개수 값 리스트, 정답
    if index == n: #피연산자가 모두 사용되었을 경우
        ans[0] = max(ans[0], value)
        ans[1] = min(ans[1], value)
        return
    for mode in range(4):
        if operator_cnt[mode] <= 0:
            continue
        operator_cnt[mode] -= 1
        next_value = calculate(mode, value, operand[index])
        backtracking(next_value, index + 1, n, operand, operator_cnt, ans)
        operator_cnt[mode] += 1

def solution(n, operand, operator_cnt): #피연산자 개수, 피연산자 값 리스트, 연산자 개수 값들
    ans = [-INF, INF] #ans[0]: max_value, ans[1]: min_value
    backtracking(operand[0], 1, n, operand, operator_cnt, ans) #첫번째 피연산자값, 1, 피연산자 개수, 피연산자 값 리스트, 연산자 개수 값 리스트, 정답
    return ans

if __name__ == "__main__":
    n = int(input()) #피연산자 개수
    operand = list(map(int, input().split())) #피연산자
    operator_cnt = list(map(int, input().split())) #각 연산자 개수

    ans = solution(n, operand, operator_cnt)

    print(int(ans[0]))
    print(int(ans[1]))