a = [10, 2, 23, 17, 33]
prefix = [0] * len(a)
prefix[0] = a[0]

for i in range(1, len(a)):
    prefix[i] = prefix[i-1] + a[i]

print(prefix)