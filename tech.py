num=3025
s=len(str(num))
if s%2==0:
    fh=num//10**(s//2)
    sh=num%10**(s//2)
    if num==(fh+sh)**2:
        print("Tech Number")
    else:
        print("Not a Tech Number")
else:
    print("Not a Tech Number")
    