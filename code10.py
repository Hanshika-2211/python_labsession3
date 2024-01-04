# Write a program to remove all the duplicates from the given list
list=[1,2,3,4,5,6,7,6,5,4]
newlist = []
for element in list:
    if element not in newlist:
        newlist.append(element)
print("Original List with Duplicates:", list),print("List without Duplicates:", newlist)

