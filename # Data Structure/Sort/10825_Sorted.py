import sys

sys.stdin = open('10825.txt', 'r')
N = int(sys.stdin.readline())
Information = []

for _ in range(N): # O(n)
    data = sys.stdin.readline().split()
    int_data = list(map(int, data[1:]))
    data[1:] = int_data
    Information.append(data)

result = sorted(Information, key = lambda x : (-x[1], x[2], -x[3], x[0]))
for i in range(len(result)):
    print(result[i][0])
