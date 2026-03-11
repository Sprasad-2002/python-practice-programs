s='abbcd how are you hello abbcd'
l=[]
word=''
for ch in s:
    if ch==' ':
        l=[word]+l
        word=''
    else:
        word=ch+word
l=[word]+l
print(l)
