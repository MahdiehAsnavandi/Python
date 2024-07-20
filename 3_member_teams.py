candidates = int(input())
experience = input()
experience = experience.split()
count_member = 0
for i in experience:
    i = int(i)
    if i <= 2:
        count_member = count_member + 1
count_team = count_member // 3
print(count_team)        