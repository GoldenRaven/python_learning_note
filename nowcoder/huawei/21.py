while True:
    try:
        s = input()
        l1 = [0]
        l2 = [0]
        for i in range(1, len(s)):
            max_ = 0
            j = 1
            while True:
                if (i-j >= 0) and (i+j < len(s)) and (s[i-j] == s[i+j]):
                    max_ += 1
                    # print(i, j, s[i-j], s[i+j])
                else:
                    if max_ == 0:
                        l1.append(max_)
                    else:
                        l1.append(max_*2+1)
                    break
                j += 1
        # print(l1)
        for i in range(1, len(s)):
            max_ = 0
            j = 1
            while True:
                if (i-j >= 0) and (i+j-1 < len(s)) and (s[i-j] == s[i+j-1]):
                    max_ += 1
                    # print(i, j, s[i-j], s[i+j])
                else:
                    l2.append(max_*2)
                    break
                j += 1
        # print(l2)
        l1.extend(l2)
        print(max(l1))
    except:
        break
