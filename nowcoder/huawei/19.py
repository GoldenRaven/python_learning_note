def Encrypt(aucPassword):
    aucResult = ''
    for i in aucPassword:
        if i.isalpha():
            if i == 'z':
                aucResult = aucResult + 'A'
            elif i == 'Z':
                aucResult = aucResult + 'a'
            else:
                aucResult = aucResult + chr(ord(i)+1).swapcase()
        elif i.isdigit():
            if i == '9':
                aucResult = aucResult + '0'
            else:
                aucResult = aucResult + chr(ord(i)+1)
        else:
            aucResult = aucResult + i
    return aucResult

def unEncrypt(password):
    result = ''
    for i in password:
        if i.isalpha():
            if i == 'a':
                result = result + 'Z'
            elif i == 'A':
                result = result + 'z'
            else:
                result = result + chr(ord(i)-1).swapcase()
        elif i.isdigit():
            if i == '0':
                result = result + '9'
            else:
                result = result + chr(ord(i)-1)
        else:
            result = result + i
    return result

while True:
    try:
        s1 = input()
        s2 = input()
        ans1 = Encrypt(s1)
        ans2 = unEncrypt(s2)
        print(ans1)
        print(ans2)
    except:
        break
