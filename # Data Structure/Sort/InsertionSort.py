def insertion_sort(unordered):
    for i in range(1, len(unordered)):
        key = unordered[i] # 딜러가 건네 준 카드

        j = i
        while j > 0 and unordered[j - 1] > key: # key 값보다 해당 값이 클 때 까지
            unordered[j] = unordered[j - 1]
            j -= 1
        unordered[j] = key

test = [45, 23, 87, 12, 32, 4]
insertion_sort(test)

print(test)
