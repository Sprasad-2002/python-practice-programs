num=13121
sum=0
dup=num
while num>0:
    rem=num%10
    sum=sum*10+rem
    num//=10
if dup==sum:
    print('Palindrome')
else:
    print('not a Palindrome')