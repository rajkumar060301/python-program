# 6.wap to print element of array of even qurry.
list = []
n = int(input("Enter size of array: "))
for i in range(0, n + 1):
    element = int(input())
    list.append(element)
print(list)
for num in list:
    if (num % 2 == 0):
        print(num, end=" ")
