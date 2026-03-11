num=27
val=0
while val*val*val<=num:
    if val*val*val==num:
        print('perfect Cube')
        break
    else:
        val+=1
else:
    print('not a Pefect Cube')