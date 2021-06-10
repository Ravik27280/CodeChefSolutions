# def Div():
#     n=int(input())
#     l=[]
#     fn=[]
#     for i in range(n):
#         a=list(map(int,input().split()))
#         l.append(a)
#     for i in range(n):
#         s1=(l[i][2]/l[i][0])+(l[i][3]/l[i][1])
#         fn.append(int(s1))
#     for i in fn:
#         print(i)
# Div()

T=int(input())
for i in range(T):
    D,d,p,q=map(int,input().split())
    x=D//d
    if x%2==0:
        c=d*((x//2)*(2*p+(x-1)*q))
        c+=(D%d)*(p+x*q)
    else:
        c=d*(x*(p+((x-1)//2)*q))
        c+=(D%d)*(p+x*q)
    print(int(c))
