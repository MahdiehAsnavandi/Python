word = input()
reversed_word = word[::-1]
print(reversed_word)
word_lower = word.lower()
reversed_word_lower = reversed_word.lower()

if word_lower == reversed_word_lower:
    print("palindrome")
else:
    print("not plandrome")    
