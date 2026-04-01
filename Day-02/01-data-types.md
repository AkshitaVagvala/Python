In programming, a data type is a classification or categorization that specifies which type of value a variable can hold. Data types are essential because they determine how data is stored in memory and what operations can be performed on that data. Python, like many programming languages, supports several built-in data types. 
Suppose you are writing python programme, so you write a file with extension .Py, And you write something called "Akshita" because as human being you can understand that it is Akshita as a name but for compliers and interpreters, anything you write in a file is only a data for compilers. Whether you write numbers, names, decimals, everything you write is a data for compilers or programs. So they need to understand what is the type of the data. That is why every programming language has Data Types. So every programming language has data types like string, float, integer etc….
How the compiler will understand its string, numeric is through Syntax. 

Syntax means how you are declaring a particular variable or writing that particular value. So if just write Akshita, then complier doesn't understand that its String you need to put that in double quotes or single quotes. Then Python will understand a person is writing a list of character or a string. 

In python we don't need to mention int or float like 6 or 6.3, like in other languages like golang we will mention as var, int like that…  So this type of Python laguage is Dynamic typed language. 

Here are some of the common data types in Python:
    1. String Data Type: 
    2. Numeric Data Types:
        ○ int: Represents integers (whole numbers). Example: x = 5
        ○ float: Represents floating-point numbers (numbers with decimal points). Example: y = 3.14
        ○ complex: Represents complex numbers. Example: z = 2 + 3j
    3. Sequence Types:
        ○ str: Represents strings (sequences of characters). Example: text = "Hello, World"
        ○ list: Represents lists (ordered, mutable sequences). Example: my_list = [1, 2, 3] ----

        1. List (Mutable)
        
        my_list = [1, 2, 3]
        my_list[0] = 10
        print(my_list)
        👉 Output:
        
        [10, 2, 3]
        ✔ You can:
            • Add (append) 
            • Remove (remove) 
            • Modify values 
        ○ tuple: Represents tuples (ordered, immutable sequences). Example: my_tuple = (1, 2, 3)

“Lists are mutable sequences, whereas tuples are immutable sequences used for fixed data.”
    4. Mapping Type:
        ○ dict: Represents dictionaries (key-value pairs). Example: my_dict = {'name': 'John', 'age': 30}
    5. Set Types:
        ○ set: Represents sets (unordered collections of unique elements). Example: my_set = {1, 2, 3}
        ○ frozenset: Represents immutable sets. Example: my_frozenset = frozenset([1, 2, 3])
    6. Boolean Type:
        ○ bool: Represents Boolean values (True or False). Example: is_valid = True
    7. Binary Types:
        ○ bytes: Represents immutable sequences of bytes. Example: data = b'Hello'
        ○ bytearray: Represents mutable sequences of bytes. Example: data = bytearray(b'Hello')

bytes and bytearray both store binary data, but bytes is immutable while bytearray can be modified. 

        Why do we need bytes?
        Used when working with:
            • Files (images, videos)  
            • Network data (APIs, sockets) 
            • Encoding/decoding text

        ○ b'Hello' → raw binary version of text           
        ○ bytes → fixed 
        ○ bytearray → editable

        Type	Meaning
        bytes	Locked data 🔒 (cannot change)
        bytearray	Editable data ✏️ (can change)
    8. None Type:
        ○ NoneType: Represents the None object, which is used to indicate the absence of a value or a null value.
    9. Custom Data Types:
        ○ You can also define your custom data types using classes and objects.
        
        

        
        
        
        Inbuilt Functions: For every programme there will be a inbuilt functions so Python has the Inbuilt functions which is maintained and managed by Python and don't need to write much code. 
        
        For eg: we got task like we need to get the details of the first name only. So using python we can get the full of all the persons and later we use the inbuilt function string.split ("-") and then we can get the first name. 
        So whenever we are using any programme then search for Inbuilt Functions. 
        

        
        For every data type there will be Inbuilt functions like For strings, For Numeric, and for sequence.. So when ever in interview or everywhere use the inbuilt functions. Later use any other way. 
        
        So always learn the inbuilt funtion of each and every data type. 
        
