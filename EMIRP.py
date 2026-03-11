num=13
count=0
for val in range(1,num+1):
    if num%val==0:
        count+=1
if count==2:
    sum=0
    dup=num
    while num>0:
        sum=sum*10+(num%10)
        num//=10
    if sum!=dup:
        count2=0
        for val2 in range (1,sum+1):
            if sum%val2==0:
                count2+=1
        if count2==2:
            print('Emirp')
        else:
            print('not EMIRP') 
    else:
        print('not emirp') 
else:
    print('not emirp')       
