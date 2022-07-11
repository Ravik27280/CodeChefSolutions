t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    malti=max(l)
    l.remove(malti)
    addition=max(l)
    diff=pow((addition-(4*malti)),1/2)
    print(diff)

    print(l)