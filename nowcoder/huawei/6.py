num = int(input())
n = num
l = []
i = 2
while ( i <= n ):
    # print(i, n, l)
    if ( n%i == 0 ):
        l.append(i)
        n = n/i
        i = 2
        # print(i, n)
        continue
    if ( i == n ):
        l.append(i)
        break
    # print(i, n, l)
    # print()
    i = i + 1
l_sort = sorted(l)
s = str(l_sort[0]) + ' '
for i in range(1, len(l)):
    s = s + str(l_sort[i]) + ' '
print(s)
