import re

# Sample text
text = "The rain in Spain stays mainly in the plain."
search = "spain"
result = re.search(search, text, re.IGNORECASE)
if result:
    print("search found:", search)
else:
    print("search not found:", search)
    