# learning sets in python

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# set1 and set2 are two sets in python

# union of set1 and set2 is the set of all elements in set1 and set2

print("Union of set1 and set2: ", set1.union(set2))

print("Union of set1 and set2: ", set1|set2)

 # intersection of set1 and set2 is the set of all elements which are in both set1 and set2 

print("Intersection of set1 and set2: ", set1.intersection(set2)) 

print("Intersection of set1 and set2: ", set1 & set2) 

# difference of set1 and set2 is the set of all elements in set1 but not in set2 

print("Difference of set1 and set2: ", set1.difference(set2)) 

print("Difference of set1 and set2: ", set1 - set2) 

# symmetric difference of set1 and set2 is the set of elements in either set1 or set2 but not in both 

print("Symmetric difference of set1 and set2: ", set1.symmetric_difference(set2)) 

print("Symmetric difference of set1 and set2: ", set1 ^set2)

  
