data = []
rows = 0;
columns = 0;
tmp_array = [];
choosen_numbers = [];

# file1 = open('data.txt', 'r')
# Lines = file1.readlines()

# counter = 0;
# for line in Lines:
#     if counter == 0:
#         rows = line
#     elif counter == 1:
#         columns = line
#     else:
#         tmp = []
#         for num in line:
#             data.append(line.split())
#     counter+=1;
data = [[-2, 1,3],[1,-2,5],[1,-1,6]]

min_num = (min(data[0]))
choosen_numbers.append(min_num)

for x in (n+1 for n in range(len(data)-1)):
    for i in range(len(data[x])):
        tmp_array.append(min_num+data[x][i])
        print(min_num+data[x][i])
    tmp_min = min(tmp_array)
    index = tmp_array.index(tmp_min) - 1
    print('\n')
    print(index, data[x][index])
    print('\n')
    choosen_numbers.append(data[x][index])

print(choosen_numbers)
Sum = sum(choosen_numbers)
print(Sum)

#         tmp_array.append(min_num+data[x][i])
#     print(tmp_array)