word = input()

if "AB" in word:
    x = word.replace("AB", "")
    if "BA" in x:
        print("YES")
    else:
        print("NO")
else:
    print("NO")                