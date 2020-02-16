def my_key(string):
    return string.upper()
while True:
    try:
        s = input()
        # s = 'A Famous Saying: Much Ado About Nothing (2012/8).'
        l = []
        ll = []
        for i, v in enumerate(s):
            if not v.isalpha():
                l.append((i, v))
            else:
                ll.append(v)
        ss = sorted(ll, key=my_key)
        for i in range(len(l)):
            # print((l[i][0], l[i][1]))
            ss.insert(l[i][0], l[i][1])
        print(''.join(ss))
    except:
        break

# s = 'asdf234GDSdsf23'
# def key1(y):
#     yy = (y.isdigit(),y.isdigit() and int(y) % 2 == 0,y.isupper(),y)
#     print(yy)
#     return yy
# ss = sorted(s, key=key1)
# print(ss)
