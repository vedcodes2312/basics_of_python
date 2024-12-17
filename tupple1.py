#tupple in python

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Accessing elements in a tuple
print(tuple1[0])  # Output: 1
print(tuple2[1])  # Output: 5

# Concatenation
tuple3 = tuple1 + tuple2
print(tuple3)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
tuple4 = tuple1 * 2
print(tuple4)  # Output: (1, 2, 3, 1, 2, 3)

# Intersection
tuple5 = (1, 2, 3, 4, 5)
tuple6 = (4, 5, 6, 7, 8)
intersection = set(tuple5) & set(tuple6)
print(intersection)  # Output: {4, 5}

# Union
tuple7 = (1, 2, 3, 4, 5)
tuple8 = (4, 5, 6, 7, 8)
union = set(tuple7) | set(tuple8)
print(union)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Symmetric difference
tuple9 = (1, 2, 3, 4, 5)
tuple10 = (4, 5, 6, 7, 8)
symmetric_difference = set(tuple9) ^ set(tuple10)
print(symmetric_difference)  # Output: {1, 2, 3, 6, 7, 8}

 