num_labtop = int(input())
p_q = input()
p_q = p_q.split()
count = 1
price = []
quality = []

for i in p_q:
    price.append(int(p_q[0]))
    quality.append(int(p_q[1]))
    count = count + 1
    if count <= num_labtop:
        p_q = input()
        p_q = p_q.split()
    
print(price)
print(quality)

for p in price:
    for r in price :
        if p < r:
            pi = price.index(p)
            ri = price.index(r)
            if quality[pi] > quality[ri]:
                print("happy irsa")
            elif quality[pi] < quality[ri]:
                print("poor irsa")    
