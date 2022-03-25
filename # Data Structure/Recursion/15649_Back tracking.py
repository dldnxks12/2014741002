def permute(ans):
    if len(ans) == M:
        print(*ans)
    else:
        for s in range(1, N+1):
            if s not in ans:
                ans.append(s)
                permute(ans)
                ans.pop()

N, M = map(int, input().split())
permute([])
