data = []
rows = 0;
columns = 0;
tmp_array = [];
choosen_numbers = [];

def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]


def select_elements(matrix):
    # Sort each row of the matrix in ascending order
    sorted_matrix = [sorted(row) for row in matrix]
    
    # Initialize the selected elements list
    selected = [0] * len(matrix)
    
    # Select the smallest absolute value from each row
    for i, row in enumerate(sorted_matrix):
        min_val = float('inf')
        for val in row:
            if abs(val) < abs(min_val):
                min_val = val
        selected[i] = min_val
    
    return selected

file1 = open('data.txt', 'r')
Lines = file1.readlines()

counter = 0;
for line in Lines:
    if counter == 0:
        rows = line
    elif counter == 1:
        columns = line
    else:
        tmp = []
        tmp = line.split()
        to_int = []
        for i in range(len(tmp)):
            to_int.append(int(tmp[i]))
        data.append(to_int)
    counter+=1;

# data = [[-2, 1,3],[1,-2,5],[1,-1,6]]

min_num = closest(data[0],0)
choosen_numbers.append(min_num)

for x in (n+1 for n in range(len(data)-1)):
    tmp_array = []
    for i in range(len(data[x])):
        tmp_array.append(min_num+abs(data[x][i]))
    tmp_min = closest(tmp_array,0)
    index = tmp_array.index(tmp_min) - 1
    choosen_numbers.append(data[x][index])

selected = select_elements(data)
print(sum(selected))

#         tmp_array.append(min_num+data[x][i])
#     print(tmp_array)

