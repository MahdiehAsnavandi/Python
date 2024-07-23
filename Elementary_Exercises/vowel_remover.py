def anti_vowel():
    a = input()
    b = "aeouiAEOUI"
    for i in b:
        if i in a:
            a = a.replace(i , "")
    a = a.lower()
    a = ".".join(a)
    return(a)    


print(anti_vowel()) 

