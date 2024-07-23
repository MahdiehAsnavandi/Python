Letters = input().lower()
h = Letters.find("h")
e = Letters.find("e")
l = Letters.find("l")
l2 = Letters.find("l" , l+1)
o = Letters.find("o")

if h < e < l < l2 < o:
    print("YES")
else:
    print("NO")
