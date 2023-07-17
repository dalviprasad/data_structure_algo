def gcd(a, b):
    # Assume a >= b
    if b > a:
        a, b = b, a

    if a % b == 0:
        return b
    else:
        diff = a - b
        return gcd(max(b, diff), min(b, diff))


print(gcd(101, 2))
