def f(n):
    for i in range(3):
        b = bin(n)[2:]
        s = sum(list(map(int, str(n))))
        if s % 2 == 0:
            b += '0'
        else:
            b += '1'
        n = int(b, 2)
    return n

print(f(17))
