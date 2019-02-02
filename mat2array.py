mat = [[1, 2], [0, 3, 4], [8, 7, 6, 5]]

mat2array = [num for array in mat for num in array]

mat2array.sort()

print(mat2array)
