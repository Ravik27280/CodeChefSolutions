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

TestCase=int(input())
l=[]
s=0
n=1
Ans=[]

for i in range(TestCase):
    a=list(map(int,input().split()))
    l.append(a)

print(l)
# for i in range(l[0]):
#     if i/l[1]==0:
#         s+=l[2]+n*l[3]
#         r=s
#         n+=1
#     else:
#         s+=r
# print(s-l[1])
for i in range(len(l)):
    for j in range(l[i][0]):
        r=l[i][2]
        if j%l[i][1]==0:
            s+=l[i][2]+(n*l[i][3])
            r=s
            n+=1
        else:
            s+=r
    Ans.append(s)
    s=0
    n=1
for i in range(len(Ans)):
    print(Ans[i])
