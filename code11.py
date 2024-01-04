# Write a program to add two matrices by using nested list
x=[[2,5,4],[1,3,9],[7,6,2]]
y=[[1,8,5],[7,3,6],[4,0,9]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j] 

print("Matrix X:")
for row in x:
    print(row)
print("Matrix Y:")
for row in y:
    print(row)
print("Sum of Matrices X,Y and Z:")
for row in result:
    print(row)