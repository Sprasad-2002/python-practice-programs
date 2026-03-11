num=131
sum=0
place=10**(len(str(num))-1)
dup=num
while num>0:
    rem=num%10
    sum=sum+rem*place
    num//=10
    place//=10
if dup==sum:
    print('Palindrome')
else:
    print('not a palindrome')
        