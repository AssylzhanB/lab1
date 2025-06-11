import re

text = "abb abbb abbbb ab a"
matches = re.findall(r'ab{2,3}', text)
print(matches)
