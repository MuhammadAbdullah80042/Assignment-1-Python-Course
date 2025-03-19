# VARIABLE AND DATA TYPES

# 1. Declare three variables: an integer, a float, and a string. Print their types.
integer = 1
float = 1.2
string = "My name is Abdullah"
print("This is an Integer: " "1" ,type(integer)) 
print("This is float: ", "1.2", type(float)) 
print("This is a string:","My name is Abdullah", type(string)) 

# 2. Convert a float num = 12.7 to an integer and a string. Print the results

num = 12.7
a = int(num)
b = str(num)
print("As Integer:", a)
print("As String", b)

# 3. Convert x = '25' (a string) to an integer and a float. Print the results.

x ='25'
i = int(x)
f = float(x)
print("Integer: ", i)
print("Float: ", f)

# 4. Check the datatype and mutability of given variables: a=10, b='Hello', c=3.14, etc.

# Mutable: Values can be modified
# Immutable: Valies cannot be modified
# To find datatype of a variable we will use type() function

a = 10
b = 'Hello'
c = 3.14


print ("Datatype of variable 'a' :", type(a))
print (f"Datatype of variable 'b' :", type(b))
print (f"Datatype of variable 'c' :", type (c))

print(f"Variable 'a' = Immutable ")
print(f"Variable 'b' = Immutable")
print(f"Variable 'c' = Immutable")
 
# 5. Create a dictionary with variable names as keys and values as different datatypes.

# This dictionary stores student number of each student. 
dict = {
     
    "Ali" : 234553,
    "Abdullah" : 72829,
    "Ibrahim" : 32453,
    "Zahid" : 89806,
}

print (dict["Ali"])
print (dict["Zahid"])
#---------------------------------------