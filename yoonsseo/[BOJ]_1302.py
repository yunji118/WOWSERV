N = int(input())

books = dict()

#딕셔너리에 키가 있으면 값 +1, 없으면 생성
for _ in range (N) :
    b = input()
    if b in books :
        books[b] += 1
    else :
        books[b] = 1

num = max(books.values())
best = [k for k, v in books.items() if v == num]
best.sort()
print(best[0])