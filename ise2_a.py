
list1 = [2, 3, 4, 5, 6]
val = 7
pairs = []

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] + list1[j] == val:
            pairs.append((list1[i], list1[j]))

print("Pairs:", pairs)
