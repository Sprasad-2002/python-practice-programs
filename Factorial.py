num=0
fact=1
if num>=0:
    for val in range(num,0,-1):
        fact*=val
    print(fact)
else:
    print('fact not possible')