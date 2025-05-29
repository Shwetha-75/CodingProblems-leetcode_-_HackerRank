import re#regular expression to find the matching string
st="aabbD"
if re.findall("[a-zA-Z0-9]",st):print(True)
else:
    print(False)
if re.findall("[a-zA-Z]",st):print(True)
else:
    print(False)
if re.findall("[0-9]",st):print(True)
else:
    print(False)

if re.findall("[a-z]",st):print(True)
else:
    print(False)
if re.findall("[A-Z]",st):print(True)
else:
    print(False)