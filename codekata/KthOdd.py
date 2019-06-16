G,H=map(int,input().split())
J=list(map(int,input().split()))
K=[]
for i in J:
  if(i%2!=0):
    K.append(i)
print(K[H-1])
