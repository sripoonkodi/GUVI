F,v=map(int,input().split())
def GCD(F,v):
    if(v==0):
        return F
    else:
        return GCD(v,F%v)
j=GCD(F,v)
print(j)
