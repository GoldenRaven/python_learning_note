while True:
    try:
        key = input().lower()
        data = input()
        # key = 'ligaoyang'
        # data = 'ni hAO'
        l = [list(key).index(x) for x in key]
        # print(l)
        index_ = list(set(l))
        ll = [key[i] for i in index_]
        alpha = []
        for i in range(26):
            a = ord('a') + i
            alpha.append(chr(a))
        while len(ll) < 26:
            for i in alpha:
                if i not in ll:
                    ll.append(i)
        # ll1 = ''.join(ll)
        print(''.join(alpha))
        print(''.join(ll))
        data2 = []
        for i in range(len(data)):
            if data[i].isalpha() and data[i].isupper():
                data2.append(ll[alpha.index(data[i].lower())].upper())
            elif data[i].isalpha() and data[i].islower():
                data2.append(ll[alpha.index(data[i].lower())].lower())
            else:
                data2.append(data[i])
        data2 = ''.join(data2)
        print(data2)
    except:
        # print('error')
        break
    # finally:
        # break
