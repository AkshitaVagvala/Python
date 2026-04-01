Keywords are reserved words in Python that have predefined meanings and cannot be used as variable names or identifiers. These words are used to define the structure and logic of the program. They are an integral part of the Python language and are case-sensitive, which means you must use them exactly as specified.

Here are some important Python keywords:

and: It is a logical operator that returns True if both operands are true.

or: It is a logical operator that returns True if at least one of the operands is true.

not: It is a logical operator that returns the opposite of the operand's truth value.

if: It is used to start a conditional statement and is followed by a condition that determines whether the code block is executed.

else: It is used in conjunction with if to define an alternative code block to execute when the if condition is False.

elif: Short for "else if," it is used to check additional conditions after an if statement and is used in combination with if and else.

while: It is used to create a loop that repeatedly executes a block of code as long as a specified condition is true. Runs code again and again as long as condition is True
Example: count = 1

while count <= 3:
    print(count)
    count += 1 # output = 123

    Note: Condition checked before each loop
Stops when condition becomes False

for: It is used to create a loop that iterates over a sequence (such as a list, tuple, or string) and executes a block of code for each item in the sequence. Used to iterate(repeat) over a sequence (list, string, etc.)
Eg:
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
    #output 
apple
banana
orange
Note: 
Automatically loops through each item
No need to manage index manually

in: Used with for, it checks if a value is present in a sequence. Checks membership (exists or not)
Eg: fruits = ["apple", "banana"]

print("apple" in fruits) # Output - True
Also used in loops:
Eg:
fruits = ["apple", "banana", "orange"]

for x in fruits:
    print(x)
Note: Take each item from fruits one by one and store it in x 

try: It is the beginning of a block of code that is subject to exception handling. It is followed by except to catch and handle exceptions.Try to run this code (which might cause an error). 

except: Used with try, it defines a block of code to execute when an exception is raised in the corresponding try block.If an error happens, handle it instead of crashing

finally: Used with try, it defines a block of code that is always executed, whether an exception is raised or not.Always run this code, no matter what happens

****“Try to run code, if error occurs handle it, and always run the final step.”

Even simpler:
try → try it
except → handle error
finally → always run

Note:
Flow:
try → run the code
If error happens → go to except
If no error → skip except
finally → always runs (in both cases)

*****def: It is used to define a function in Python. def is used to define a function, and a function is a reusable block of code that performs a specific task (not just arithmetic operations). Function = a small reusable program inside your program
Why use functions?
Avoid repeating code
Make code cleaner
Easy to reuse. Also, Think of function like: 📦 A machine — you give input → it gives output

*****return: It is used within a function to specify the value that the function should return.

*****class: It is used to define a class, which is a blueprint for creating objects in object-oriented programming.A class is a blueprint, and objects are instances created from that class.

🧠 Simple relationship:
Class → design / template
Object → real instance (created from class)

class Car:
    pass

car1 = Car()
car2 = Car()

👉 Here:

Car → class ✅
car1, car2 → objects ✅

*****🧠 Better way to say it:

“Objects are instances of a class”

****** 🔥 Simple analogy:
Class = 🍪 cookie cutter
Object = 🍪 cookies

👉 One cutter → many cookies

🧠 Key idea:
Class defines structure
Object uses that structure

******import: It is used to import modules or libraries to access their functions, classes, or variables.

***** from: Used with import to specify which specific components from a module should be imported.

****** as: Used with import to create an alias (alternative) for a module, making it easier to reference in the code.

True: It represents a boolean value for "true."

False: It represents a boolean value for "false."

None: It represents a special null value or absence of value.

is: It is used for identity comparison, checking if two variables refer to the same object in memory.

lambda: It is used to create small, anonymous functions (lambda functions).

with: It is used for context management, ensuring that certain operations are performed before and after a block of code.

global: It is used to declare a global variable within a function's scope.

nonlocal: It is used to declare a variable as nonlocal, which allows modifying a variable in an enclosing (but non-global) scope.