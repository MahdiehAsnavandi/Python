a = input()
b = []
for i in a:
    if i != "+":
        b.append(i)
b.sort()

def string_maker():
    x = ''
    for l in b:
        x = x + str(l) + ''
    return("+".join(x))

print(string_maker())

    