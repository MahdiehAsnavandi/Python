word = input()
low_word = word.lower()
up_word = word.upper()
small = 0 
Captal = 0

for i in word:
    for l in low_word:
        for u in up_word:
            if i == l:
                small = small + 1
            elif i == u:
                Captal = Captal + 1    
if Captal <= small:
    print(low_word)
else:
    print(up_word)    