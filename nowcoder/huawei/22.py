while True:
    try:
        s1 = input()
        s2 = input()
        # s1 = '10.0.3.193'
        # s1 = '0.0.1.0'
        # s2 = 256
        ss1 = [int(i) for i in s1.split('.')]
        sss1 = [0 <= x <= 255 for x in ss1]
        check = True
        for i in range(len(sss1)):
            check = check and sss1[i]
        if not check:
            raise IOError
        else:
            l = []
            for i in range(len(ss1)):
                b = bin(ss1[i])[2:]
                l.append(b)
                # print(b)
            m = 8
            ll = ['0'*(m-len(l[i]))+l[i] for i in range(len(l))]
            ll = int(''.join(ll),2)
            print(ll)
        ss2 = bin(int(s2))[2:]
        # print(ss2)
        if len(ss2) > 32:
            raise IOError
        else:
            ss3 = []
            if len(ss2)%8 == 0:
                for i in  range(0,len(ss2)//8):
                    ss3.append(ss2[8*i:8*(i+1)])
            else:
                ss3.append(ss2[0:len(ss2)%8])
                for i in  range(0,(len(ss2)//8)):
                    ss3.append(ss2[len(ss2)%8+8*i:len(ss2)%8+8*(i+1)])
        sss = ['0', '0', '0', '0']
        for i in  range(len(ss3)):
            sss[3-i] = str(int(str(ss3[len(ss3)-1-i]), 2))
            # print(i, sss[3-i])
        # print(sss)
        ans = '.'.join(sss)
        print(ans)
    except IOError:
        print('IP illegal')
        break
    except:
        break
