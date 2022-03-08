list = []
traverse = []
count = 0
a = 5
b = 20
for i in range(a, b):
    list.append(i)
print(list)
for j in list:
    if (j % 2 != 0):
        traverse.append(j)
print(traverse)
for k in traverse:
    count = count + 1
print(count)
