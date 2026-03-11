a=12
b=13
if a > b:
    great = a
else:
    great = b
while(True):
    if great % a == 0 and great % b == 0:
        lcm=great
        break
    great+=1
print(lcm)