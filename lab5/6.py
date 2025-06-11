import re

text = "acb a123b a___b axxxb ab a-b"
matches = re.findall(r'a.*b', text)
print(matches)
