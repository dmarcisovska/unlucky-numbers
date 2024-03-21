
for i in range(1,21):

    if i == 4 or i == 13:
        print(i, " is UNLUCKY")
    elif i % 2 == 0 and i != 4:
        print(i, " is even")
    elif i % 2 != 0 and i != 13:
        print(i, "is odd")

