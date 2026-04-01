import re

text = "The rain in Spain stays mainly in the plain."
search = "spain"
search = "the"
result = re.match(search, text, re.IGNORECASE)
if result:
    print("match found:", search)
else:
    print("match not found:", search)
