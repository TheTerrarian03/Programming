image1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list = []
list2 = []
list3 = []

for item1 in range(len(image1)):
    for item2 in image1[item1]:
        list.append(item2)

print(list)

for i in range(-1, len(list) - 1):
    list2.append(list[i])

print(list2)

x = 0
for i in range(len(image1)):
    temp_list = []
    for i2 in range(len(image1[0])):
        temp_list.append(list2[x])
        x += 1
    list3.append(temp_list)

print(list3)

