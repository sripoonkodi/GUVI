NN=int (input())
if NN>1:
      for i in range(2,NN):
       if (NN%i) == 0:
           print("no")
           break
      else:
       print("yes")
else:
   print("no")
