def combine(ans):
    if len(ans) == M:
        print(*ans)
    else:
        for s in range(1, N+1):
            # list의 길이가 0인데 ans[-1] 이런거 하면 바로 에러 뜬다
            # 따라서 아래의 두 조건의 순서를 바꾸면 에러가 뜬다.
            if len(ans) > 0 and s <= ans[-1]:
                continue
            else:
                ans.append(s)
                combine(ans)
                ans.pop()

N, M = map(int, input().split())
combine([])
