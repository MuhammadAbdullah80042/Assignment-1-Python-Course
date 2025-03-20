#  "Sets - Practical Questions"

 # 1. Create a set with five unique numbers and print it.
a = {1, 2, 3, 4, 5, 6, 7}
print(a)

# 2. Add an element to a set and remove an element from it. Print the result.
a = {1, 2, 3, 4, 5, 6, 7}
a.add(6)
a.remove(1)
print(a)

# 3. Create two sets and perform union, intersection, and difference operations.
a = {1, 2, 3, 4, 5, 6, 7}
b = {6, 7, 8, 9, 10}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# 4. Convert a list with duplicate values into a set and print the unique elements.
a = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3]
b = set(a) # When we convert a list into sets it removes the duplicate values automatically.
print(b)

# 5. Check if a given element exists in a set and print an appropriate message.
a = {1, 2, 3, 4, 5, 6, 7}
if 5 in a:
    print("Yes")
else:
    print("No")


# 6. Create a set of vowels and check if 'z' is present in the set or not.

vowels = {'a', 'e', 'i', 'o', 'u'}
if z in a:
    print("Z Exists")
else:
    print("Z does not exist")


# 7. Try adding a list as an element inside a set. What happens? Explain.

a = {1, 2, 3, 4, 5, 6, 7}
a.add([8, 9, 10]) # Lists are mutable, so they cannot be hashed and added to a set.
print(a) # We will get a type error.    


# 8. Convert a set into a sorted list and print the result.

a = {1, 2, 3, 4, 5, 6, 7}
b = sorted(a)
print(b)

# ----------------------------------------------------------------------------------------------------