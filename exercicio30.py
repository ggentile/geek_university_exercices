import numpy as np

r = int(input("Select the row size of the matrix: "))
c = int(input("Select the column size of the matrix: "))

print("Select the values inside of the matrix in one line, split by space: ")

entries = list(map(int, input().split()))

matrix = np.array(entries).reshape(r, c)
print(matrix)

if np.any(matrix[:c] > matrix[:r]):
    a = (np.dot(2, r)) + (np.dot(7, c)) - 2

elif np.any(matrix[:r] > matrix[:c]):
    a = (np.dot(4, np.dot(r, r, r))) - (np.dot(5, np.dot(c, c))) + 1

else:
    a = (np.dot(3, np.dot(r, r))) - 1

print(a)
# check lines 13 and 15 the error when handling with a matrix of different row and column
# Note: For some stupid matter, numpy has trouble when multiplying numbers that not match
# when it comes to a row and column differences. Go back to the exercise and do it the other way

