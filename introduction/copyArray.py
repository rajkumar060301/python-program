# 4.wap to copy all the element one array to another array.

list = []
for i in range(1, 5 + 1):
    element = int(input())
    list.append(element)
anotherArray = list.copy()
print(anotherArray)
