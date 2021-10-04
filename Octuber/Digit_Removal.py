# cook your dish here
try:
    t=int(input())
    for i in range(t):
        n,d=map(str,input().split())
        check=d in n
        count=0
        while d in n:
            n=int(n)+1
            n=str(n)
            count+=1
        
        print(count)
except:
    pass