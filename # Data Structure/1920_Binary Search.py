import sys
import bisect

def binary_search(ordered_list, item):
    left, right = 0, len(ordered_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if item < ordered_list[mid]:
            right = mid - 1
        elif item > ordered_list[mid]:
            left = mid + 1
        else:
            return mid
    return None

sys.stdin = open('1920.txt', 'r')

N = int(input())
card = list(map(int, input().split()))
card.sort()
M = int(input())
target = list(map(int, input().split()))

for m in target:
    if binary_search(card, m) is not None:
        print("1")
    else:
        print("0")

