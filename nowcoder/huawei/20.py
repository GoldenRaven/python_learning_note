while True:
    try:
        s = input()
        i = 0
        while i < len(s):
            if not s[i].isalpha():
                s = s.replace(s[i], ' ')
            i += 1
        l = s.split()
        ss = ''
        for i in range(len(l)-1, 0, -1):
            ss += l[i] + ' '
        ss += l[0]
        print(ss)
    except:
        break
