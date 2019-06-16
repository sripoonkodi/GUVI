n,k=map(int,input().split())
d=input()
l=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in m:
    l.append(i)
    print(max(l),end=" ")
