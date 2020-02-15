s = input()
l = s.split()
l.reverse()
ss = l[0] + ' '
for i in range(1, len(l)-1):
    ss = ss + l[i] + ' '
ss = ss + l[-1]
print(ss)
