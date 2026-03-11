num=789321
place=10**(len(str(num))-1)
sum=0
while num>0:
    rem = num%10
    sum=sum+rem*place
    num//=10
    place//=10
print(sum)