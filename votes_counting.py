n = int(input())
countries = input()
votes = {}
count = 1
while count < n:
    if countries in votes:
        votes[countries] += 1
        countries = input()
        count = count + 1 
    else:
        votes[countries] = 1
        countries = input()
        count = count + 1 

for i in votes:
    print(i , votes[i])