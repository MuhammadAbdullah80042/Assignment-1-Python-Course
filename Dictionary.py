# Dictionaries

#  1. Create a dictionary with country names as keys and capitals as values.

a = {  # Taken names from AI
    "Spain": "Madrid",
    "Italy": "Rome",
    "Egypt": "Cairo",
    "South Korea": "Seoul",
    "Mexico": "Mexico City"
}

print(a)

#  2. Add a new key-value pair and print the updated dictionary.

a = { # Taken names from AI
    "Spain": "Madrid",
    "Italy": "Rome",
    "Egypt": "Cairo",
    "South Korea": "Seoul",
    "Mexico": "Mexico City"
}
a["Argentina"] = "Buenos Aires"
print(a)

# 3. Store student info (name, age, grade) in a dictionary and print the grade.

a = {
    "name": "Abdullah",
    "age": 19,
    "grade": "A+"
}

print(a["grade"]) 

# 4. Update the age in a student dictionary and print the result.

a = {
    "name": "Abdullah",
    "age": 19,
    "grade": "A+"
}
a["age"] = 20
print(a)

# 5. Create a phonebook dictionary and check if 'John' exists in it.

a = {   # Taken names from AI
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}
print(a["John"]) # This will give an error because John is not in the dictionary.

# 6. Remove a key from a dictionary and print the updated dictionary.

a = {  # Taken names from AI    
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}
a.pop("Bob")
print(a)

# 7. Store book info (title, author, year, price) and print the price.

a = { # Taken names from AI
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988,
    "price": 10.99
}
print(a["price"])

# 8. Convert a dictionary's keys into a list and print them

b = { # Taken names from AI
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988,
    "price": 10.99
}
c = list(b.keys())
print(c)

# 9. Merge two dictionaries into one and print it.

a = { # Taken names from AI
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988,
    "price": 10.99
}
b = {   # Taken names from AI
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}

a.update(b)
print(a+b)

#--------------------------------------------------------------------------------------