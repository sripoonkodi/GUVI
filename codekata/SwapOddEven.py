I=input()
for i in range(len(I)):
  if (i%2==0):
    print(I[i+1],end='')
  else:
    print(I[i-1],end='')
