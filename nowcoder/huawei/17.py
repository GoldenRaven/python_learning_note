while True:
    try:
        s = input()
        l = list(s)
        # print(l)
        ll = [l.count(x) for x in l]
        # print(ll)
        min_ = min(ll)
        # print(min_)
        while True:
            try:
                lll = ll.index(min_)
                l.pop(lll)
                ll.pop(lll)
                # print(lll,ll)
                # print(l)
            except:
                ss = l[0]
                for i in l[1:]:
                    ss = ss + i
                print(ss)
                break
    except:
        break
