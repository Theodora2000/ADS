# https://www.programiz.com/dsa/kruskal-algorithm
data = []
lowest = 0

file1 = open("data_kruskal.txt", "r")
Lines = file1.readlines()

for line in Lines:
    list_of_strings = line.split(" ")
    list_of_integers = list(map(int, list_of_strings))
    data.append(list_of_integers)

print("Unsorted", data)

num = []

for i in range(len(data)):
    num.append(data[i][2])

num.sort()

sorted = []

for i in range(len(num)):
    for j in range(len(data)):
        if num[i] == data[j][2]:
            sorted.append(data[j])
            continue


new_k = []
for elem in sorted:
    if elem not in new_k:
        new_k.append(elem)
sorted = new_k
print("Sorted", sorted)
