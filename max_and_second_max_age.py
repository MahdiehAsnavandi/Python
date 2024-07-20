age = int(input())
ages = []


while age != -1:
    if 10 < age < 90 and age not in ages:
        ages.append(age)
        age = int(input())
    else:
        age = int(input())
        continue          

print(ages)
max_list = max(ages)
ages.remove(max_list)
second_max_list = max(ages)
print(max_list , second_max_list)    
   

         


