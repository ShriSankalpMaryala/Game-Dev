matrix = [[0,1,2,3],
          [4,5,6,7],
          [8,9,10,11]]
print(matrix[2][2])
print(matrix[1][0])
print(matrix)

for i in matrix:
    print(i)          

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j],end=" ")
    print()

matrix.reverse()
print(matrix)


# HOMEWORK
# reverse the order of values inside the rows also
# matrix.reverse()
# print(matrix)

          