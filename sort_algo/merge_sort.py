def merge(list1, list2):
    fin_list = []
    a, b = len(list1), len(list2)
    i, j = 0, 0
    while i + j < a + b:
        if i == a:
            fin_list.append(list2[j])
            j += 1
        elif j == b:
            fin_list.append(list1[i])
            i += 1
        elif list1[i] <= list2[j]:
            fin_list.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            fin_list.append(list2[j])
            j += 1
    return fin_list


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
fin_list = merge(list1, list2)
print(fin_list)


def mergesort(list3, left, right):
    if (right - left) <= 1:
        return list3[left:right]
    if (right - left) > 1:
        mid = (right + left) // 2

        left_list = mergesort(list3, left, mid)
        right_list = mergesort(list3, mid, right)

        return merge(left_list, right_list)


list3 = [
    3,
    7,
    7,
    6,
    98,
    4,
    5,
    6,
    9,
    4,
    3,
    36,
]

print(mergesort(list3, 0, len(list3)))
