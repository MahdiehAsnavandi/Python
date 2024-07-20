def divisors():
    divisors_count = 0
    number = int(input())
    for i in range(1 , number + 1):
        if number % i == 0:
            divisors_count = divisors_count + 1
    return(number , divisors_count)


count_num = 0
x = []
a = []
while count_num < 20:
    number , divisors_count = divisors()
    x.append(divisors_count)
    a.append(number)
    count_num = count_num + 1 

max_divisor = max(x)
index_divisor = x.index(max(x))
for i in a:
    if a.index(i) == index_divisor:
        print(i , max_divisor)





