import re

text = "hello_world test_case python_script"
matches = re.findall(r'[a-z]+_[a-z]+', text)
print(matches)
