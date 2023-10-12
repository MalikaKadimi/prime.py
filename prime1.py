Num = int(input())
i=1
res = True
while i<=Num:
    if (i!=1 and Num%i==0 and i!=Num):
        res = False
        break
    i+=1
if (res == True):
       print("prime num")
else:
       print("not a prime num")