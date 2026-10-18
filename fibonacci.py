def first(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    l = [0, 1]
    for i in range(2, n):
        l.append(l[i - 2] + l[i - 1])
    return l


if __name__ == '__main__':
    n = int(input())
    print(first(n))