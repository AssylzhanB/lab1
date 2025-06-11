import re

text = "a ab abb abbb ac"
matches = re.findall(r'ab*', text)
print(matches)
