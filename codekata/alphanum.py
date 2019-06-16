N=input()
M=[]
for i in N:
  if (i.isnumeric()):
    M.append(i)
print(*M,sep='')
