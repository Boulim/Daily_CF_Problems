"""
感叹🐏太强的一题
"""
#python代码：
n, mod = map(int, input().split())
p = []
for _ in range(n):
    l, r = map(int, input().split())
    p.append((r // mod - (l - 1) // mod) / (r - l + 1))
ans = 0
for i in range(n):
    ans += p[i] + p[i - 1] - p[i] * p[i - 1]
print(ans * 2000)
