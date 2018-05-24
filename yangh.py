#杨辉三角
def triangles():
    # n = 0
    # L1 = [1, 0]
    # while True:
    #     if n == 0 :
    #         yield L1[:-1]
    #     elif n == 1 :
    #         L1.insert(1, 1)
    #         yield L1[:-1]
    #     else:
    #         L = []
    #         L.insert(0, 1)
    #         for i in range(1, n):
    #             L.insert(i, L1[i-1] + L1[i])
    #         L.insert(len(L), 1)
    #         yield L
    #         L1 = L
    #     n = n + 1
    # return 'done'

    L = [1]
    yield L
    L = L + [1]
    yield L
    while True:
        L = [1] + [L[i] + L[i+1] for i in range(0, len(L) -1 )] + [1]
        yield L


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
