"""
思路： 矩阵周长是 2 * (a + b)， 矩阵面积是 a * b
那么目标最小值是 4 *(a + b) ** 2 // a * b = 4 *(a / b + 2 + b / a) = 8 + 4 * (a/ b + b / a) = 8 + 4 * (a ** 2 + b ** 2) / (a * b)

只要找到差值最小的两个数就可以了 ？不对，喜提wa

还是按照原来做吧， 差点超时
"""
#python代码:
t = int(input())
for _ in range(2 * t):
    n = input()
    a = list(map(int, input().split()))
    c = Counter(a)
    c2 = []
    for k, v in c.items():
        if v >= 4:
            print(k, k, k, k)
            break
        elif v >= 2:
            c2.append(k)
    else:
        if len(c2) >= 2:
            c2.sort()
            a, b = c2[0],c2[1]
            for i in range(2, len(c2)):
                if (c2[i] ** 2 + c2[i - 1] ** 2) * a * b < (b ** 2 + a** 2) * c2[i]*c2[i - 1]:
                    b, a = c2[i],c2[i - 1]
            print(a, a, b, b)
