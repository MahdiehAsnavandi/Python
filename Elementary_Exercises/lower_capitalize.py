a = input()
count = 1
names = []
while count <= 10:
    # a = a[:1].upper() + a[1:].lower()    OR
    a = a.lower().capitalize()
    names.append(a)
    a = input()
    count = count + 1

for l in names:
    print(l)    
    
