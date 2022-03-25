import sys
import bisect


def binary_search(ordered_list, item):
    index = bisect.bisect_left(ordered_list, item)

    if index < len(ordered_list) and ordered_list[index] == item:
        return index
    else:
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

