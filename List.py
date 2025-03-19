# List

# 1. Create a list of five fruits and print the second and last element.

a=["Orange", "Grapes", "Apple", "Peach", "Mangoes"]
print("Second Fruit is:", a[1]) # Python starts counting from 0. So, the second fruit will be at [1].
print("The last fruit is:", a[-1]) # [-1] points to the last element in the list.

#  2. Add a fruit at the start and end of the list, then print it.

c=["Orange", "Grapes", "Apple", "Peach", "Mangoes"]
c.insert(0,"Banana")
c.append("Melon") # append is used to add an element in the end.
print(c)

# 3. Remove the third element from the list and print it

b=["Orange", "Grapes", "Apple", "Peach", "Mangoes"]
b.pop(2)
print(b)

# 4. Replace the second element in [10, 20, 30, 40, 50] with 25.

d=[10, 20, 30, 40, 50]
d[1]=25
print(d)

# 5. Concatenate two lists and print the result.

e=[1, 2, 3, 4, 5]
f=[6, 7, 8, 9, 10]
g=e+f
print(g)

# 6. Extract elements from index 1 to 4 using slicing.

a=[1,2,3,4,5,6,7,8,9,10]
print(a[1:4:])

# 7. Create a list with an integer, string, and float. Print each element's type.

v=[8,"Abdullah",13.9]
print(type(v[0]))
print(type(v[1]))
print(type(v[2]))

#------------------------------------------------------