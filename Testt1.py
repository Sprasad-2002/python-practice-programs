def Arm(num,sum=0):
    dup=num
    power=len(str(num))
    while num>0:
        rem=num%10
        sum=sum+rem**power
        num=num//10
    return sum==dup
print(list(filter(Arm,range(1,101))))