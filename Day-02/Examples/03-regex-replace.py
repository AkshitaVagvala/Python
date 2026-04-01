import re

text = "The rain in Spain stays mainly in the plain."
replacement = "cloud"
modified_text = re.sub("spain", replacement, text, flags=re.IGNORECASE)
print("Modified text:", modified_text)

text1 = "Karthiv is cute and Karthiv is smart."
replacement1 = "handsome"
modified_text1 = re.sub("cute", replacement1, text1)
#re.sub() replaces ALL matches by default, so only the first "cute" will be replaced, not the second one.
#“re.sub() is used to replace occurrences of a pattern in a string with a specified value.”
print("modified_text:", modified_text1)
