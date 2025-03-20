strs="/?appcmek $ jnkc@kkdk"
s=""
for i in strs:
    if ((i>="A" and i<="Z") | (i>="a" and i<="z") | (i==" ")):
        s = s+i
print(s)
