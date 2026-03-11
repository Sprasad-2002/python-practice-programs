num = 5
space = num - 1

for ev in range(num,0,-1):
    for sp in range(1, space + 1):
        print(" ", end=" ")   
    for col in range(num,  ev-1, -1):
        print(col, end=" ")
    print()
    space -= 1
