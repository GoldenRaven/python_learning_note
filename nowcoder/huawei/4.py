while True:
    try:
        s = input()
        l =  []
        length = len(s)
        a = length/8
        b = length%8
        if b == 0 :
            l_len = 0
            for i in range(int(a)+l_len):
                l.append(s[i*8:(i+1)*8])
        else:
            l_len = 1
            for i in range(int(a)+l_len-1):
                l.append(s[i*8:(i+1)*8])
            c = s[-b:]
            l.append(c + '0'*(8-b))
        for i in range(len(l)):
            print(l[i])
    except:
        break
