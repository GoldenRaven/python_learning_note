while True:
    try:
        s = input()
        l = [ord(x) for x in s]
        ll = sorted(l)
        ss = [chr(x) for x in ll]
        print(''.join(ss))
    except:
        break
