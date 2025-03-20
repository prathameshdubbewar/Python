s="vinayak vasant takale"
l=[]
for i in  range (len(s)):
    if s[i]==" ":
        l.append(i)
l.append(len(s))
print(l)

out=[]
j = 0
for i in range(len(l)):
    out.append(s[j:l[i]])
    j = l[i] + 1

print(out)

str = ""

for i in out:
    str += i + " "

print(len(str) -1)

