t=int(input())
for i in range(t):
    count=2
    x,y,a,b=map(int,input().split())
    if (x==a or x==b):
        count-=1
    if(y==a or y==b):
        count-=1
    print(count)
    count=0