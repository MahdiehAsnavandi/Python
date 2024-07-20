score = int(input("what is the score? "))
count = 1

if score == 3:
    win_count = 1
else:
    win_count = 0  

sum_score = score      

while count < 30:
    score = int(input("what is the score? "))
    sum_score = sum_score + score
    count = count + 1
    if score == 3:
        win_count = win_count + 1
print(sum_score , win_count)
