#import re
#text = "orange , apple, banana, grape"
#pattern = r","
#result = re.split(pattern, text)
#print("split_txt:" , result)

import re

text = "apple,banana,orange,grape"
strcture = r","
split_result = re.split(r",", text)
print("Split result:", split_result)
#note: When working with regex, developers always use r by habit because:
# Most regex patterns use \
# It avoids future bugs
# Keeps code consistent
#"," if your text contains all those separators(comma, space, semicolon), "[,; ]" - Works for mixed separators