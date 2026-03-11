num=182
sum=0
dup=num
while num>0:
    rem=num%10
    sum=sum+rem
    num//=10
if dup%sum==0:
    print('niven')
else:
    print('not niven')