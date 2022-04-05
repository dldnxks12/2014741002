import sys

# 학생 N명의 이름 - 국어 - 영어 - 수학

# 1. 국어 점수가 감소하는 순서
# 2. 국어와 영어가 같으면 수학 적수가 감소하는 순서
# 3. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서

sys.stdin = open('10825.txt', 'r')
N = int(sys.stdin.readline())
Information = []

for _ in range(N): # O(n)
    data = sys.stdin.readline().split()
    int_data = list(map(int, data[1:]))
    data[1:] = int_data
    Information.append(data)

# sort()는 List의 멤버함수 -> sort() 사용 시 기존 list가 바뀐다
# sorted()는 외부에서 만든 함수 -> 기존 list 바뀌지 않는다.
Information.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in range(len(Information)):
    print(Information[i][0])
