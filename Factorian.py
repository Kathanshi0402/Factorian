j=0
while j<=40585:    #40585 is the largest factorian
    n=j
    temp=n
    f=0
    while n>0:
        a=n%10
        fact=1
        for i in range(1,a+1):
            fact=fact*i       #To find factorial of "a"
        f=f+fact
        n=n//10
    if temp==f:
        print(temp)
    j=j+1
