XA, YA, XB, YB, XC, YC = map(int,input().split())

AB = ( (XA-XB)**2 + (YA-YB)**2 )**0.5
AC = ( (XA-XC)**2 + (YA-YC)**2 )**0.5
BC = ( (XC-XB)**2 + (YC-YB)**2 )**0.5
length = [AB, AC, BC]
length.sort()

if length[2] < length[1] + length[0] :
    ans = (length[2] - length[0])*2
    print(ans)
else :
    print(-1.0)