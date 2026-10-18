def two(n, a):
    prevMap = {}
    for i in range(len(a)):
        diff = n - a[i]
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[a[i]] = i
if __name__ == '__main__':
    a = [3, 4, 5, 6]
    target = 7
    print(two(target, a))