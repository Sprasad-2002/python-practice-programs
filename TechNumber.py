num=2025
sum=0
s=(len(str(num)))
if s%2==0:
    half=10**(s//2)
    fh=num//half
    sh=num%half
    if num==(fh+sh)**2:
        print('TEch')
    else:
        print('not a TEch')
else:
    print('not a Possible')