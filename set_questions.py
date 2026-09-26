# 1) Create a set with values 1, 2, 3, 4 .
my_set = {1, 2, 3, 4}
print(my_set)
# Output: {1, 2, 3, 4}
# 2) Add the value 5 to the set 1, 2, 3, 4 using a set method.
my_set = {1, 2, 3,4}
my_set.add(5) 
print(my_set)  
# Output: {1, 2, 3, 4, 5} 
# 3) Remove the value 3 from the set 1, 2, 3, 4 using a set method.
my_set = {1, 2, 3, 4}
my_set.remove(3)
print(my_set)  
# Output: {1, 2, 4} 
# 4) Check if 2 exists in the set 1, 2, 3, 4 .
my_set = {1, 2, 3, 4}
print(2 in my_set)
# Output: True
# 5) Convert the list 1, 2, 2, 3, 4, 4 into a set to remove duplicates.
list1 = [1, 2, 2, 3, 4, 4]
my_set = set(list1)
print(my_set)
# Output: {1, 2, 3, 4}
# 6) Convert the tuple 10, 20, 30 into a set.
my_tuple = (10, 20, 30)
my_set = set(my_tuple)
print(my_set)
# Output: {10, 20, 30}
# 7) Find the union of sets 1, 2, 3 and 3, 4, 5 .
set1 = {1, 2, 3} 
set2 = {3, 4, 5} 
result = set1.union(set2)
print(result)  
# Output: {1, 2, 3, 4, 5} 
# 8) Find the intersection of sets 1, 2, 3 and 3, 4, 5 .
set1 = {1, 2, 3} 
set2 = {3, 4, 5} 
result = set1 & set2 
print(result)  
# Output: {3} 
# 9) Find the difference between sets 1, 2, 3, 4 and 3, 4 .
set1 = {1, 2, 3, 4} 
set2 = {3, 4} 
result = set1 - set2 
print(result)  
# Output: {1, 2} 
# 10) Create a copy of the set 5, 6, 7 using a set method.
set1 = {5, 6, 7} 
set2 = set1.copy() 
print(set2)  
# Output: {5, 6, 7} 
# 11) Remove all elements from the set 1, 2, 3 using one set method.
my_set = {1, 2, 3} 
my_set.clear() 
print(my_set)  
# Output: set() 
# 12) Check whether 1, 2 is a subset of 1, 2, 3 .
set1 = {1, 2} 
set2 = {1, 2, 3} 
print(set1.issubset(set2))  
# Output: True 
# 13) Check whether 1, 2, 3 is a superset of 1, 2 .
set1 = {1, 2, 3} 
set2 = {1, 2} 
print(set1.issuperset(set2))  
# Output: True 
# 14) Find the symmetric difference between 1, 2, 3 and 3, 4, 5 . 
set1 = {1, 2, 3} 
set2 = {3, 4, 5} 
result = set1 ^ set2 
print(result)  
# Output: {1, 2, 4, 5} 
# 15) Add multiple elements 8, 9, 10 into  1, 2, 3 using a set method .
set1 = {1, 2, 3} 
set2 = {8, 9, 10} 
set1.update(set2) 
print(set1)  
# Output: {1, 2, 3, 8, 9, 10} 
# 16) Remove a random element from the set 1, 2, 3 using a set method.
my_set = {1, 2, 3} 
removed_item = my_set.pop() 
print(removed_item)  
# Output: 1
# 17) Check if two sets 1, 2, 3 and 3, 2, 1 are equal.
set1 = {1, 2, 3}
set2 = {3, 2, 1}
print(set1 == set2)
# Output: True
# 18) From the list 1, 2, 2, 3, 4, 4, 5 , extract only unique values using a set.
my_list = [1, 2, 2, 3, 4, 4, 5]
unique = set(my_list)
print(unique)
# Output: {1, 2, 3, 4, 5}
# 19) Convert the set 1, 2, 3 into a list.
my_set = {1, 2, 3}
my_list = list(my_set)
print(my_list)
# output: [1, 2, 3]
# 20) From 1, 2, 3, 4, 5 , remove 2, 4 using a set method.
set1 = {1, 2, 3, 4, 5} 
set2 = set1.difference({2,4})
print(set2)  
# Output: {1, 3, 5} 