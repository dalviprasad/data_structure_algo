def gcd(a, b):
    i = min(a, b)
    while i > 0:
        if (a % i == 0) and (b % i == 0):
            return i
        else:
            i -= 1


print(gcd(14, 63))
