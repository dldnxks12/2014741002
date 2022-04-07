# 11729 Hanoi Tower
N = int(input())

def hanoi(disk_number, source, destination, extra):
    if disk_number == 1:
        hanoi.count += 1
        hanoi.moves.append((source, destination))
    else:
        hanoi(disk_number-1, source, extra, destination)
        hanoi.count += 1
        hanoi.moves.append((source, destination))
        hanoi(disk_number-1, extra, destination, source)

hanoi.count = 0
hanoi.moves = []
hanoi(N, 1, 3, 2)

print(hanoi.count)
for i in range(len(hanoi.moves)):
    print(hanoi.moves[i][0],hanoi.moves[i][1])

