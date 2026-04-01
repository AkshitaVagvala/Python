        Regex - Regex is a way to search, match, and manipulate text using patterns
        1. Regular Expressions for Text Processing:
            • Regular expressions (regex or regexp) are a powerful tool for pattern matching and text processing means Regex is a way to find, check, or extract specific patterns from text. 

            • Eg: Pattern matching
            👉 Finding a specific format in text
            Example:
                • Find all emails in a file 
                • Find phone numbers 
                • Check if a password is valid 
Text processing
                👉 Working with text like:
                    • Extracting data 
                    • Replacing words 
                    • Cleaning logs 
        🧾 Example:
                    Text:
                    My email is test@gmail.com
                    Regex helps you:
                        • ✔ Find email 
                        • ✔ Extract it 
                        • ✔ Validate format
            • The re module in Python is used for working with regular expressions.
            • Common metacharacters: . (any character), * (zero or more), + (one or more), ? (zero or one), [] (character class), | (OR), ^ (start of a line), $ (end of a line), etc.

            1. Find all numbers
            Regex:
            \d+
            👉 Matches:   
            123, 456, 789
            2. Find all emails
            Regex:
            \S+@\S+\.\S+
            👉 Matches:
            test@gmail.com
            abc@yahoo.com
            
            3. Find words starting with “a”
            Regex:
            \ba\w*
            
            🔹 Common Metacharacters (Super Important)
            Symbol	Meaning	Example
            .	Any character	a.b → acb, a1b
            *	0 or more	ab* → a, ab, abb
            +	1 or more	ab+ → ab, abb
            ?	0 or 1	ab? → a, ab
            []	Specific characters	[abc] → a or b or c
            `	`	OR
            ^	Start of string	^Hello
            $	End of string	end$

            • Examples of regex usage: matching emails, phone numbers, or extracting data from text.
            • re module functions include re.match(), re.search(), re.findall(), and re.sub() for pattern matching and replacement.

EXAMPLE OF REGREX: 

import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

🔍 What your code does

import re
👉 Imports the regular expression module


text = "The quick brown fox"
pattern = r"brown"
    • text → the sentence 
    • pattern → what you want to find 
👉 r"brown" means raw string (good practice in regex)


search = re.search(pattern, text)
👉 This checks:
    “Is the word brown present anywhere in the text?”
✔ It searches the entire string


if search:
    • If found → search is not None 
    • If not found → search is None 


print("Pattern found:", search.group())
👉 search.group() returns the matched text
👉 Output will be:

Pattern found: brown

🧠 Simple understanding:
    • re.search() → finds pattern anywhere 
    • group() → gives the matched result 

🔥 What if pattern not found?

pattern = r"cat"
👉 Output:

Pattern not found

🔍 Important note:
    • re.search() → finds first match only 
    • If you want all matches → use re.findall() 

✅ Final summary:
    Your code searches for the word “brown” in the text and prints it if found.

💬 Interview one-liner:
    “re.search() is used to find the first occurrence of a pattern in a string and returns a match object if found.”
    
    
    Function	What it does
    match()	Checks pattern at start only
    search()	Finds first match anywhere
    findall()	Returns all matches (list)
