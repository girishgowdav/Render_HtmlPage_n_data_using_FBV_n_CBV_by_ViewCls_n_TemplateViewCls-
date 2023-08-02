
s='afmx'
p=''
for i in s:
    p+=chr((ord(i)+3))
print(p)


l=['p23y+1','@21th','x78yz']
l1=l.copy()
for i in range(len(l1)):
    z=0
    for j in l1[i]:
        if j.isdigit():
            z+=int(j)
    l1[i]=z
print(l)
print(l1)
    