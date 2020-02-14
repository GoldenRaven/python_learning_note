n = int(input())
d = {}
while True:
    try:
        for i in range(n):
            s = input()
            l = s.split(' ', 1)
            if (l[0] in d.keys()):
                d[l[0]] = d[l[0]] + int(l[1])
                # print(d[l[0]])
            else:
                d[l[0]] = int(l[1])
                # print(d[l[0]])
            # print(l)
            l2 = [int(i) for i in d.keys()]
            l3 = sorted(l2)
        for k in l3:
            print(k, d[str(k)])
    except:
        break
