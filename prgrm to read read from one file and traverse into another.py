f1=open("QUOTE.TXT", "r")
f2=open("VOW.TXT", "w")
s=f1.read()
vow=['a','e','i','o','u']
flag=0
for ch in s:
    if(ch.lower() in vow):
        f2.write(ch+" ")
        flag=1
if(flag==0):
    print("No vowels to write!")
else:
    print("Vowels exported successfully.")
f1.close()
f2.close()
