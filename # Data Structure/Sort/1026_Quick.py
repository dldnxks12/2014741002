import sys

def pivot_index(unordered, first_index, last_index, mode):
    pivot = unordered[first_index]
    left_pointer  = first_index + 1
    right_pointer = last_index

    if mode == 1:
            while True:
                while unordered[left_pointer] <= pivot and left_pointer < last_index:
                    left_pointer  += 1
                while unordered[right_pointer] > pivot and right_pointer > first_index:
                    right_pointer -= 1
                if left_pointer < right_pointer:
                    unordered[left_pointer], unordered[right_pointer] = unordered[right_pointer], unordered[left_pointer]
                else:
                    break
            unordered[first_index], unordered[right_pointer] = unordered[right_pointer], unordered[first_index]
    else:
        while True:
            while -unordered[left_pointer] <= -pivot and left_pointer < last_index:
                left_pointer  += 1
            while -unordered[right_pointer] > -pivot and right_pointer > first_index:
                right_pointer -= 1

            if left_pointer < right_pointer:
                unordered[left_pointer], unordered[right_pointer] = unordered[right_pointer], unordered[left_pointer]
            else:
                break

        unordered[first_index], unordered[right_pointer] = unordered[right_pointer], unordered[first_index]
    return right_pointer

def quick_sort(unordered, first, last, mode):
        if first < last:
            pivot_idx = pivot_index(unordered, first, last, mode)
            quick_sort(unordered, first, pivot_idx - 1, mode)
            quick_sort(unordered, pivot_idx+1, last, mode)

sys.stdin = open('1026.txt', 'r')
N = int(sys.stdin.readline())            # 1026.txt의 첫 번째 line
A = list(map(int, sys.stdin.readline().split())) # 1026.txt의 두 번째 line
B = list(map(int, sys.stdin.readline().split())) # 1026.txt의 세 번째 line
C = B.copy() # New Object

quick_sort(A, 0, len(A)-1, 1)
quick_sort(C, 0, len(A)-1, 2)

SOP = 0
for a, b in zip(A,C):
    SOP += (a*b)

print(SOP)


