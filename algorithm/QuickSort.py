def partition(arr, low, high):
    i = low
    pivot = arr[high]

    print('low = %d, high = %d' % (low, high))
    for j in range(low, high):
        print('j = %d' % j, ',', arr[j], pivot)
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# array = [3, 1, 2, 5, 4, 1, 4, 5, 7, 9, 11, 10]a
array = [3, 2, 1, 4]
quickSort(array, 0, len(array) - 1)

print('ans = ', array)
