import re
text="9618793063 thifdasdfghkll ,8897946942dfghjkk,6300773243sdfghjklkhgf"
a=re.findall(r"[8 9][0-9]{9}",text)
for i in a:
    print(i)
            
