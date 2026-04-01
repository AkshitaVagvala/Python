import re
text = "The quick brown fox jumps over the lazy dog"
find_all = "jumps"
result = re.findall(find_all , text)
print("found word:",result)

