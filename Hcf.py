a=10
b=12
if a < b:
    small = a       
else:
    small = b
while True:
    if a % small == 0 and b % small == 0:
        hcf=small
        break
    small-=1
print(hcf)