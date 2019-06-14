m=list(input())
if len(m)%2==0:
  m[int(len(m)/2)]='*'
  m[int(len(m)/2)-1]='*'
else:
  m[int(len(m)/2)]='*'
for i in range(0,len(m)):
  print(m[i],end='')


