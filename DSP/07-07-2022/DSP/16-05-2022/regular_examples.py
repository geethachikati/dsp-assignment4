import re
text="Anu is 19,Geetha is 20,Vandana is 21,Laxmisri is 24"
a=re.findall(r"[A-Z][a-z]+",text)
b=re.findall(r"[0-9]{2}",text)
d={}
i=0
for name in a:
    d[name]=b[i]
    i+=1
print(a)
print(b)
print(d)
