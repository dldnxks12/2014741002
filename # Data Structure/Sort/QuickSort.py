# Merge Sort와 비슷하게, Unordered List를 2개의 Sublist로 쪼개고 divide and conquer paradigm을 사용
# Left Pointer가 가르키는 값이 Pivot보다 크면 오른쪽으로 이동
# Right Pointer가 가르키는 값이 Pivot보다 크면 왼쪽으로 이동
# 두 포인터가 Stop되면 Swap
# 두 포인터의 위치가 바뀌면 Right Point가 가르키는 값과 Pivot 값을 Swap
# Pivot을 기준으로 다시 Sublist로 쪼개서 divide and conquer until whole list sorted

def partition(unsorted, first, last): # Argument : Unsorted list, 첫 번째 Index, 마지막 Index
    pivot = unsorted[first] # 가장 왼쪽 Index를 Pivot으로

    left  = first + 1 # Left Pointer
    right = last     # Right Pointer

    while True:
        while unsorted[left] <= pivot and left < last: # Left Pointer가 가르키는 값이 Pivot 보다 작다면 오른쪽으로 이동
            left += 1
        while unsorted[right] > pivot and right >= first: # Right Pointer가 가르키는 값이 Pivot보다 크다면 왼쪽으로 이동
            right -= 1

        if left < right:
            unsorted[left], unsorted[right] = unsorted[right], unsorted[left] # Swap
        # left > right
        else: # Left < Right 라면 즉, left pointer와 right pointer가 순서가 바뀌면 ...
            break

    # pivot과 right pointer value swap
    unsorted[first], unsorted[right] = unsorted[right], unsorted[first]
    return right # Pivot Index

def Quick_sort(unsorted, first, last):
    if first < last: # List의 길이가 1이 되면 Base case  ...
        pivot_index = partition(unsorted, first, last)
        Quick_sort(unsorted, first, pivot_index - 1) # Left sublist
        Quick_sort(unsorted, pivot_index + 1, last)  # Right sublist

test = [45, 23, 87, 12, 32, 4]
Quick_sort(test, 0, len(test) - 1)

print(test)


