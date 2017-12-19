a = ["0","1","2","3","4","5","6","7","8","9"]

f = 0
s = 2

for i in a:
    # a[f:s]
    print(a[f:s])
    f += 2
    s += 2
    if a[f:s]==[]:
        break

# print()