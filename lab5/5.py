import re

text = "Hello World This Is Example test tEst"
matches = re.findall(r'[A-Z][a-z]+', text)
print(matches)
