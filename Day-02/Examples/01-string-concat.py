str = "Hello"
str2 = "World"
# Concatenating two strings using the + operator and adding a space in between(to add space between the two strings we can use " " or we can use the join method)
result = str + " " + str2
print(result)  # Output: Hello World

# Using the join method to concatenate strings, 
result = " ".join([str, str2])
print(result)  # Output: Hello World
# Note: The join method is more efficient than using the + operator for concatenating multiple strings, especially in a loop or when dealing with large strings, 
# Also " ".join(...) → puts space between items.

# Using f-strings for concatenation, using f-strings (formatted string literals) is a more modern and efficient way to concatenate strings in Python.
# A placeholder {} is like an empty slot where a value will be inserted.
result = f"{str} {str2}"
print(result)  # Output: Hello World

# Using the format method for concatenation
result = "{} {}".format(str, str2)
print(result)  # Output: Hello World
# Using the % operator for concatenation
result = "%s %s" % (str, str2)
print(result)  # Output: Hello World
