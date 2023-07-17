def gcd(a, b):
    # Assume a > b
    if a < b:
        a, b = b, a

    while a % b != 0:
        diff = a - b
        return gcd(max(diff, b), min(diff, b))
    return b


print(gcd(14, 63))
