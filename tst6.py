def int2bin(num,place=1):
    sum=0
    while num>0:
        sum+=(num%2)*place
        num=num//2
        place=place*10
    return sum
print(list(map(int2bin,range(1,21))))