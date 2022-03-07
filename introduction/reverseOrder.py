# 7.wap to array to reverse order

list = []
size = int(input("Enter the size of array: "))
for i in range(0, size):
    element = int(input())
    list.append(element)
print(list)
list.reverse()
print(list)
