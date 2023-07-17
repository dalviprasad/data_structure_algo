def gcd(a, b):
    # Assume a >= b
    if a < b:
        a, b = b, a

    while a % b != 0:
        a, b = b, a % b
    return b


print(gcd(101, 1))
print(gcd(14, 63))
