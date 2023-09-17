def recur(string, cnt) :
    if len(string) > 1 :
        cnt += 1
        Y = 0
        for x in string :
            Y += int(x)
        recur(str(Y), cnt)
    else :
        if int(string) % 3 == 0 :
            print(cnt)
            print("YES")
        else :
            print(cnt)
            print("NO")

X = input()
cnt = 0
recur(X, cnt)