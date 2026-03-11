def int2bin(num,place=1):
    if num==0:
        return 0
    return (num%2)*place+int2bin(num//2,place*10)
print(int2bin(13))