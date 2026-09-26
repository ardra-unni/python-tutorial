# Create a list 1,2,3 and add 4 to the end using a list method.
my_list=[1,2,3]
my_list.append(4)
print(my_list)
# Given 10,20,30 , remove 20 using a list method.
my_list=[10,20,30]
my_list.remove(20)
print(my_list)
# From 5,3,9,1 , sort the list in ascending order using a list method.
my_list=[5,3,9,1]
my_list.sort()
print(my_list)
# From 1,2,3,4,5 , extract 2,3,4 using slicing only.
my_list=[1,2,3,4,5]
print(my_list[1:4])
# Reverse the list 1,2,3,4 using slicing (no loops).
my_list=[1,2,3,4]
my_list.reverse()
print(my_list)
# Combine 1,2 and 3,4 into one list using list operations.
list1=[1,2]
list2=[3,4]
combined_list=list1+list2
print(combined_list)
# Convert 7,8 into 7,8,7,8 using list operations.
my_list=[7,8]
print(my_list*2)
# Check if 3 exists in 1,2,3,4 using a list operator.
my_list=[1,2,3,4]
print(3 in my_list)
# Count how many times 2 appears in 1,2,2,3,2 using a list method.
my_list=[1,2,2,3,2]
print(my_list.count(2))
# Remove the last element from ["a","b","c","d"] using a list method.
my_list=["a","b","c","d"]
my_list.pop(-1)
print(my_list)
# Insert "x" at index 1 in ["a","b","c"] using a list method.
my_list=["a","b","c","d"]
my_list.insert(1,"x")
print(my_list)
# Replace the element at index 2 in 10,20,30,40 with 99 using indexing.
my_list=[10,20,30,40]
my_list[2]=99
print(my_list)
# Convert range(5) into a list using list functions.
my_list=list(range(5))
print(my_list)
# Using slicing, extract every 2nd element from 1,2,3,4,5,6 → expected [2,4,6]
my_list=[1,2,3,4,5,6]
print(my_list[1::2])
# Remove all elements from 1,2,3 using one list method.
my_list=[1,2,3]
my_list.clear()
print(my_list)
# Copy a list 4,5,6 using only list tools (no modules).
my_list=[4,5,6]
copied_list=my_list.copy()
print(copied_list)
# Convert 1,2,3 into a nested list 1,2,3 using list operations.
list=[1,2,3]
convert_list=[list]
print(convert_list)
# Extend 1,2 with 3,4,5 using a list method.
list1=[1,2]
list2=[3,4,5]
list1.extend(list2)
print(list1)
# Using list repetition, create a list ["hello","hello","hello"] . 
my_list=["hello"]
print(my_list*3)
# remove the element at index 2 from 10,20,30,40 using a list method.
my_list=[10,20,30,40]
popped_item=my_list.pop(2)
print(popped_item)
print(my_list)
