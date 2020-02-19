n = int(input())
# n = 5
l = [[0 for i in range(n)] for j in range(n)]
count = 1
for i in range(1, n+1):
    l1 = list(range(i))
    l1.reverse()
    l2 = list(range(i))
    # print(l1, l2)
    l_index = []
    index_ = [(l1[j], l2[j]) for j in range(i)]
    # print(len(index_))
    for j in range(len(index_)):
        l[index_[j][0]][index_[j][1]] = count
        count += 1
# print(l)
for i in range(n):
    print(' '.join(map(str, l[i])).replace('0',''))
