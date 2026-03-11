num = 4
stars = 1
space = num - 1

for i in range(1, num+1):

    # print spaces
    for s in range(space):
        print(" ", end=" ")

    # print stars and hollow space
    for j in range(1, stars+1):
        if j == 1 or j == stars or i == num:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

    stars += 2
    space -= 1
