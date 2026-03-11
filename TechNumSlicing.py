num=202522
s=len(str(num))
if s%2==0:
    num1=int(str(num)[0:s//2:1])
    num2=int(str(num)[s//2:s:1])
    val=num1+num2
    if val*val==num:
        print('Tech Number')
    else:
        print('Not a Tech number')
else:
    print('Not Possible')
    
    