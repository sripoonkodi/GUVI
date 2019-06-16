V=int(input())
Y=input()
list=['a','e','i','o','u','A','E','I','O','U']
for V in range (0,len(list)):
  Y=Y.replace(list[V],'')
print (Y[::-1])
