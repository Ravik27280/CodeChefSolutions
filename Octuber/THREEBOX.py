# cook your dish here
try:
    t=int(input())
    for i in range(t):
        l=list(map(int,input().split()))
        d=l[3]
        a1=l[0]+l[1]
        a2=l[1]+l[2]
        a3=l[2]+l[0]
        a4= l[0]+l[1]+l[2]
        count=0
        if d>=a4:
            print(1)
        elif d>=a1:
            count+=1
            print(count+1)
        elif d>=a2:
            count+=1
            print(count+1)
        elif d>=a3:
            count+=1
            print(count+1)
        else:
            print(3)
except:
    pass