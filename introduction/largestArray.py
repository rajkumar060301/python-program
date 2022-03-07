# 5.wap to find the largest element to an array.

list = []
for i in range(1, 5 + 1):
    element = int(input())
    list.append(element)
anotherArray = max(list)
print("my list: ", list)
print("largest element: ", anotherArray)
