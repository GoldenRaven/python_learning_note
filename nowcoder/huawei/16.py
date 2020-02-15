def chk_passwd(s):
    i = 0
    count1, count2, count3, count4 = 0, 0, 0, 0
    while i < len(s):
        if s[i] >= 'a' and s[i] <= 'z':
            count1 = 1
            i = i + 1
            # print('a')
        elif s[i] >= 'A' and s[i] <= 'Z':
            count2 = 1
            i = i + 1
            # print('A')
        elif s[i] >= '0' and s[i] <= '9':
            count3 = 1
            i = i + 1
            # print('9')
        else:
            count4 = 1
            i = i + 1
    count = count1 + count2 + count3 + count4
    # print(count)
    def repeat():
        for i in range(len(s)):
            for j in range(i+3, len(s)-3):
                if ( s[i:i+3] == s[j:j+3] ):
                    return True
        return False
    if len(s) < 9:
        ans = 'NG'
    elif count <3:
        ans = 'NG'
        # print(2)
    elif repeat():
        ans = 'NG'
        # print(3)
    else:
        ans = 'OK'
        # print(4)
    return ans

while True:
    try:
        s = input()
        # print()
        ans = chk_passwd(s)
        print(ans)
    except:
        break
