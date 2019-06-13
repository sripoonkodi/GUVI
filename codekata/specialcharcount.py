q=input()
count=0
for i in q:
  if (i.isalnum() | (i==' ')):
    count+=0
  else:
    count+=1
    print(count)
