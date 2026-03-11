num=13
while num >9:
    sum=0
    while num>0:
        rem=num%10
        sum+=rem**2
        num//=10
    num=sum
if num==1 or num==7:
    print("Happy Number")
else:
    print("Not a Happy Number")
        