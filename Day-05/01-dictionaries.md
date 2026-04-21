# Dictionaries

## Overview:
A dictionary in Python is a data structure that allows you to store and retrieve values using keys. It is also known as a hashmap or associative array in other programming languages. Dictionaries are implemented as hash tables, providing fast access to values based on their keys.

## Creating a Dictionary:
```python
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
```
## Accessing Values:
```python
print(my_dict['name'])  # Output: John
```
**1. Do we always need ['key'] to access values?**

Not always, but that’s the standard way to get a value from a dictionary.

print(my_dict['name'])  # John

Here:

'name' is the key
['name'] means: “give me the value for this key”

👉 Important:
If the key doesn’t exist, this will throw an error (KeyError).

**Alternative (safer way):**

print(my_dict.get('name'))
.get() does not crash if the key is missing
It returns None (or a default value if you provide one)
print(my_dict.get('salary', 'Not Found'))

Note: print(my_dict.get('salary', 'Not Found'))
Why?
'salary' key does not exist in the dictionary
.get() looks for the key
If not found, it returns the default value you provided

👉 Here, the default is 'Not Found'

Compare both cases:

Without default:

print(my_dict.get('salary'))

Output:

None

With default:

print(my_dict.get('salary', 'Not Found'))

Output:

Not Found
Key idea:
.get(key) → returns None if missing
.get(key, default_value) → returns your custom value if missing

2. Why no [] in if 'age' in my_dict:?

This is a different operation.

if 'age' in my_dict:

Here you're not accessing a value, you're just checking if the key exists.

Think of it like:

'age' in my_dict → “Does this key exist?”
my_dict['age'] → “Give me the value for this key”

👉 If you used:

if my_dict['age']:

This would try to access the value, and might crash if 'age' is not present.

## Modifying and Adding Elements:
```python
my_dict['age'] = 26  # Modifying a value
my_dict['occupation'] = 'Engineer'  # Adding a new key-value pair
```

## Removing Elements:
```python
del my_dict['city']  # Removing a key-value pair
```

## Checking Key Existence:
```python
if 'age' in my_dict:
    print('Age is present in the dictionary')
```
**Iterating Through Keys and Values:**
for key, value in my_dict.items():
    print(key, value)
****
**Note:**** **   **Is .items()** **a standard method?******
Yes 👍

.items() is a built-in dictionary method.

It returns key + value pairs together.

What does this loop do?
for key, value in my_dict.items():
    print(key, value)

Yes — exactly what you said ✔️

👉 It prints both:

the key
and the value

Example output:

name John
age 25
city New York

**
**NOTE**:**
Quick Summary
my_dict['key'] → get value (can crash if key missing)
'key' in my_dict → check if key exists (safe)
my_dict.items() → get both key & value for looping



**
**If the key is a string, you must use quotes (' ')**: 

my_dict = {'name': 'John', 'age': 25}

print(my_dict['name'])   # ✅ correct

Without quotes:

print(my_dict[name])     # ❌ ERROR (Python thinks "name" is a variable)
✅ When quotes are NOT required

If the key is not a string, you don’t use quotes.

Integer key:
my_dict = {1: 'one', 2: 'two'}

print(my_dict[1])   # ✅ no quotes
Boolean key:
my_dict = {True: 'yes', False: 'no'}

print(my_dict[True])   # ✅ no quotes
🔑 Important concept
'name' → string key → needs quotes
1, True → not strings → no quotes
⚠️ Common mistake
my_dict = {'age': 25}

print(my_dict[age])   # ❌ NameError (age is not defined)

Python thinks age is a variable, not a string.

👍 Rule to remember
If your key looks like text → use quotes
If it's a number/boolean → no quotes needed

for key, value in my_dict.items():
    print(key, value)
```
