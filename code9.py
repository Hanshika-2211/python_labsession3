# Write a program to calculate the sum and mean of the given list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for number in list:
    sum += number
mean = sum / len(list)

print("List of Numbers:", list)
print("Sum of Numbers:", sum)
print("Mean (Average) of Numbers:", mean)