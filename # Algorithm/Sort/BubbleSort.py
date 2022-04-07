import sys

sys.stdin.realine()

def bubble_sort(unordered):
    iteration = len(unordered) - 1 # n-1 번 iteration
    for i in range(iteration):
        for j in range(iteration - i):
            if unordered[j] > unordered[j + 1]:
                unordered[j + 1], unordered[j] = unordered[j], unordered[j + 1]


test = [45,23, 87, 12, 32, 4]
bubble_sort(test)

print(test)




