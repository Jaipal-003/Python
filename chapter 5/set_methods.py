# Creating an empty set

b = set()
print(type(b))

# Adding values to an empty set

b.add(5)
b.add(4)
b.add(5)
b.add(5)
b.add(4)  # Adding a value repeatedly does not changes a set
b.add((7,9,0)) 
# b.add({5:6}) Cannot add list or dictionary to sets
print(b)

print(len(b))  # Prints the lenth of this set

b.remove(4) # Remove 5 from set b
# b.remove(45) # Throws an error while trying to remove 45 (which is ot present in the set)
print(b)

