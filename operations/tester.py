import re

a = "2/11/2024"

pattern_str = r'^\d{2}/\d{2}/\d{4}$'

if re.match(pattern_str, a):
    print(True)
else:
    print(False)