import re

text = "Hello, world. This is simple text"
new_text = re.sub(r"[ ,.]", ":", text)
print(new_text)
