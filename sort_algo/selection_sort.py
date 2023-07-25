def SelectionSort(list1):
    for i in range(0, len(list1)):
        min_num = i
        for j in range(i, len(list1)):
            if list1[min_num] > list1[j]:
                min_num = j
        list1[i], list1[min_num] = list1[min_num], list1[i]


l = [4, 3, 2, 1, 0]
SelectionSort(l)
print(l)
