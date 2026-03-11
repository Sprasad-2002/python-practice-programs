num=81
val=0
while val*val<=num:
    if val*val==num:
        print('perfect square')
        break
    else:
        val+=1
else:
    print('not a Pefect square')