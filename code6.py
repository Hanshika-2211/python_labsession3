# Write a program to create two sublists of even number and odd number.
numbers = [11, 22, 33, 44, 55]
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]
print("Original List:", numbers)
print("Even numbers found in the original list:", even)
print("Odd numbers found in the original list:", odd)