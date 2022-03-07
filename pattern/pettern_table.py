# 3.wap to print the following given pattern in python

n = int(input())
z = n
for i in range(0, n):
    for j in range(0, z):
        print(end=" ")
    z -= 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")
