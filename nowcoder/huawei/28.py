def getEnglishCharCount(s):
    count = 0
    for x in s:
        if x.isalpha(): count += 1
    return count

def getBlankCharCount(s):
    count = 0
    for x in s:
        if x == ' ': count += 1
    return count

def getNumberCharCount(s):
    count = 0
    for x in s:
        if x.isdigit(): count += 1
    return count

def getOtherCharCount(s):
    count = 0
    for x in s:
        if (not x.isalpha()) and (not x == ' ') and (not x.isdigit()) : count += 1
    return count

while True:
    try:
        s = input()
        print(getEnglishCharCount(s))
        print(getBlankCharCount(s))
        print(getNumberCharCount(s))
        print(getOtherCharCount(s))
    except:
        break
