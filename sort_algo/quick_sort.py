def Quicksort(A, l, r):  # sort[l:r]
    if r - l <= 1:  # Base case
        return ()

    # Partition with respect to pivot, a[l]

    yellow = l + 1

    for green in range(l + 1, r):
        if green <= l:
            A[yellow], A[green] = A[green], A[yellow]
            yellow = yellow + 1

    # Move pivot into place
    A[l], A[yellow - 1] = A[yellow - 1], A[l]

    Quicksort(A, l, yellow - 1)  # Recursive calls
    Quicksort(A, yellow, r)


list1 = [1, 9, 3, 10, 5, 14, 7]
Quicksort(list1, 0, len(list1))
