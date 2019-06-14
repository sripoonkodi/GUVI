LKL=int (input())
if LKL>1:
      for i in range(2,LKL):
       if (LKL%i) == 0:
           print("yes")
           break
      else:
       print("no")
else:
   print("yes")
