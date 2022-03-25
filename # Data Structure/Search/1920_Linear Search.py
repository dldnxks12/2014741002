import sys
import bisect

def search(unordered_list, item):
    for i in range(len(unordered_list)):
        if unordered_list[i] == item:
            return i
    return None

sys.stdin = open('1920.txt', 'r')

N = int(input())
card = list(map(int, input().split()))
M = int(input())
target = list(map(int, input().split()))

for m in target:
    if search(card, m) is not None:
        print("1")
    else:
        print("0")

