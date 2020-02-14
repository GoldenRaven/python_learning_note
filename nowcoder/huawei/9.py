s = input()
# s = '1234543234567899876'
l = [i for i in s]
l.reverse()
new = []
ss  = s[-1]
new.append(ss)
for i in l:
    if not i in new:
        new.append(i)
        ss = ss + i
print(ss)
