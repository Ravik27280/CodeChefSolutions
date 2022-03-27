l=list(map(int,input().split()))
flag=0
for i in range(3):
    if l[i]==l[3]:
        flag+=1
    else:
        pass
if flag>0:
    print("Yes")
else:
    print("No")
