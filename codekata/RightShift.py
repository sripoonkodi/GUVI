M,N=map(int,input().split())
O=list(map(int,input().split()))
for i in range(N):
  for l in range(M-1,0,-1):
    O[l],O[l-1]=O[l-1],O[l]
print(*O)
