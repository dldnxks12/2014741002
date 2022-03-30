def partition(unsorted, first, last):
    pivot = unsorted[first]

    left = first + 1
    right = last

    while True:
        while unsorted[left] <= pivot and left < last:
            left += 1
        while unsorted[right] > pivot and right >= first:
            right -= 1

        if left < right:
            unsorted[left], unsorted[right] = unsorted[right], unsorted[left]

        else:
            break

    unsorted[first], unsorted[right] = unsorted[right], unsorted[first]

    return right

def Quick_sort(unsorted, first, last):
    if first < last:
        pivot_index = partition(unsorted, first, last)
        Quick_sort(unsorted, first, pivot_index - 1)
        Quick_sort(unsorted, pivot_index + 1, last)

test = [45, 23, 87, 12, 32, 4]
Quick_sort(test, 0, len(test) - 1)

print(test)


