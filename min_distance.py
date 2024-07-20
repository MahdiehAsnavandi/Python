distances = []
x = input()
x = x.split()
for i in x:
    i = int(i)
    distances.append(i)
max_distance = max(distances)
min_distance = min(distances)
ideal = max_distance - min_distance
print(ideal)
