L=int(input())
M=list(map(int,input().split()))
N=M[:]
N.sort()
for i in range(0,len(M)):
  if(M[i]!=N[i]):
    print(i)
    break
