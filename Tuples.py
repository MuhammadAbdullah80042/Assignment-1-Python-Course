# Tuples

# 1. Create a tuple with five city names and print first and last element.

a=('New York', 'Los Angeles', 'Chicago', 'Karachi', 'Lahore')
print(a[0])
print(a[-1])

# 2. Try modifying a tuple element. Explain the error.

b=("New York","Lahore")
b[1]="Chicago"
print(b) # We will get a TypeError because we can't change the value of a tuple as they are immutable.

# 3. Convert (10, 20, 30, 40, 50) into a list, modify an element, and convert back.

c=(10,20,30,40,50)
d=list(c)
d[2]=34
e=tuple(d)
print(d)

# 4. Check if 'purple' exists in a tuple.
print("Purple"in("Green","Red","Blue","Orange","Purple"))

# 5. Unpack ('Alice', 25, 'Doctor') into separate variables and print them.
p = ("Alice", 25, "Doctor") 
a, b, c = p
print(a, b, c)

#  6. Create a mixed data type tuple and print types of each element.
a=("Ali",25,"Doctor")
print(type(a[0]))
print(type(a[1]))
print(type(a[2]))

# 7. Count occurrences of 5 in (1, 5, 2, 5, 3, 5, 4, 5).
s = (1, 5, 2, 5, 3, 5, 4, 5)  
d = s.count(5)  
print(d)

#------------------------------------------------------END------------------------------------------------------#
