# Brute Force
def bit_string(ans):
    if len(ans) == n:
        print(*ans)
    else:
        for s in data:
            ans.append(s)
            bit_string(ans)
            ans.pop()

data = 'abc'
n    = 3
bit_string([])