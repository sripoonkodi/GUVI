q=input()
c=0
for i in q:
  if (i.isalnum() | (i==' ')):
    c+=0
  else:
    c+=1
    print(c)
