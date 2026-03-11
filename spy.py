num=567
sum=0
mul=1
while num>0:
    rem=num%10
    sum+=rem
    mul*=rem
    num//=10
if sum==mul:
    print('spy number')
else:
    print('not a spy number')