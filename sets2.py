# learning sets in python 2

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5}
set3 = {6, 7, 8}

#check if set2 is a subset of set1
is_subset = set2.issubset(set1)
print("set2 is subset of set1:", is_subset)

#check if set1 is a superset of set2
is_superset = set1.issuperset(set2)
print("set1 is superset of set2:", is_superset)

#check if set1 and set3 are disjoint
are_disjoint = set1.isdisjoint(set3)
print("set1 and set3 are disjoint:", are_disjoint)

# Define a set
set4 = {1, 2, 3}
print("Initial set4:", set4)

# Add elements to set4
set4.add(4)
print("After adding 4:", set4)

# Define another set
set5 = {1, 2, 3}
print("Initial set5:", set5)

# Remove an element from set5
set5.remove(2)
print("After removing 2:", set5)

# Define another set
set6 = {3, 4, 5, 6}
print("Initial set6:", set6)

# Discard an element from set6
set6.discard(4)
print("After discarding 4:", set6)

# Define another set
set7 = {4, 5, 6, 7, 8, 9}
print("Initial set7:", set7)

# Pop an element from set7
popped_element = set7.pop()
print("Popped element:", popped_element)
print("After popping an element:", set7)

# Define another set
set8 = {3, 2, 1, 4, 5}
print("Initial set8:", set8)

# Clear set8
set8.clear()
print("After clearing:", set8)
