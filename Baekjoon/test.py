a = [1,2,3,4]
b = [5,4,3]

for x in a:
    if x not in b:
        print(x)

print([x for x in a if x not in b])