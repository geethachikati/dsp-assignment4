import re
text="this is geetha from srikakulam district"
s=re.search("geetha",text)
r=re.findall("i",text)
t=re.split("is",text)
p=re.sub("s","S",text)
print(s)
print(r)
print(t)
print(p)
