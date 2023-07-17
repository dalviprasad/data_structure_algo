def gcd(a, b):
    div_list1 = []
    div_list2 = []
    gcd_list = []
    for i in range(1, a + 1):
        if a % i == 0:
            div_list1.append(i)

    for i in range(1, b + 1):
        if b % i == 0:
            div_list2.append(i)

    for i in div_list1:
        if i in div_list2:
            gcd_list.append(i)

    return gcd_list[-1]


print(gcd(14, 63))
