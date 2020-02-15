n = int(input())
ss = []
for i in range(n):
    s = input()
    ss.append(s)
ss.sort()
# print()
for i in range(n):
    print(ss[i])
    # print(ss[i], end='\n')
