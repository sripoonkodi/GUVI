A=int(input())
B=0
C=[]
for i in range (A):
  C.append(input())
for i in range (A):
  if sorted(C[i])==sorted('kabali'):
    B+=1
print(B)
