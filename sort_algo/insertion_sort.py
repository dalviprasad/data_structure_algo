def Insertion_Sort(list1):
    for i in range(0, len(list1)):
        # Build longer and longer sorted list
        # In each iteration seq[0:i] already sorted

        # Move first element after sorted slice left
        # till it is in the correct place
        pos = i
        while (pos > 0) and (list1[pos] < list1[pos - 1]):
            list1[pos], list1[pos - 1] = list1[pos - 1], list1[pos]
            pos -= 1


l = [4, 3, 2, 1, 0]
Insertion_Sort(l)
print(l)
