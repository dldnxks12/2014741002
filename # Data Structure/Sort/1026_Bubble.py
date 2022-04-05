import sys

def bubble_sort(unordered, sign):
    iteration = len(unordered) - 1  # n-1 번 iteration
    if sign == 1:  # Ascending
        for i in range(iteration):
            for j in range(iteration - i):
                if unordered[j] > unordered[j + 1]:
                    unordered[j + 1], unordered[j] = unordered[j], unordered[j + 1]
    else:  # Descending
        for i in range(iteration):
            for j in range(iteration - i):
                if -unordered[j] > -unordered[j + 1]:
                    unordered[j + 1], unordered[j] = unordered[j], unordered[j + 1]

sys.stdin = open('1026.txt', 'r')
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
C = B.copy()

# A : ascending
# B : descending

print(A)
print(C)
bubble_sort(A, 1)  # Ascending
bubble_sort(C, -1) # Descending
print(A)
print(C)

sum_of_product = 0
for a, b in zip(A, C):
    sum_of_product += (a*b)

print(sum_of_product)





