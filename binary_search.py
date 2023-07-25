def bsearch(seq, v, l, r):
    # search for v in seq[l:r], sequence is sorted
    if l - r == 0:
        return False

    mid = l + r // 2

    if seq[mid] == v:
        return True

    if v < seq[mid]:
        return bsearch(seq, v, l, mid)
    else:
        return bsearch(seq, v, mid, r)


list1 = [1, 2, 3, 4, 5, 6, 7]

print(bsearch(list1, 10, 0, 6))
