import numpy as np

r = int(input("Select the amount of rows you want: "))
c = int(input("Select the amount of columns you want: "))

print("Write the entries in a single line separated by space: ")

entries = list(map(int, input().split()))

matrix = np.array(entries).reshape(r, c)
print(matrix)

value = matrix.max()

[(index, np.where(value)) for index, row in enumerate(matrix) if value in row]
print(value)
# verificar erro de conseguir pegar o maior valor dentro da matrix na linha 13