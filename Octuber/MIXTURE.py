
def solution(A,B):
    if A>0 and B>0:
        return "Solution"
    elif A==0:
        return "Solid"
    elif B==0:
        return "Liquid"
try:        
    t=int(input())
    for i in range(t):
        a,b= map(int,input().split())
        print(solution(a,b))
except:
    pass