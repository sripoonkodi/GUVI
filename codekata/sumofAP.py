A,B,C=map(int,input().split())
S=0
for i in range (1,C+1):
  S+=A+(i-1)*B
print(S)
