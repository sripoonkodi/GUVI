KL=int(input())
for i in range(2,KL+1):
    if(KL%i==0):
        c=0
        for j in range(1,i+1):
            if(i%j==0):
                c=c+1
        if(c==2):
            print(j,end=" ")
