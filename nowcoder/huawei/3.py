import sys
while True:
    l = []
    try:
        num = int(sys.stdin.readline())
        for i in range(num):
            n = int(sys.stdin.readline())
            l.append(n)
        sets = set(l)
        sets_sort = sorted(list(sets))
        for i in range(len(sets_sort)):
            print(sets_sort[i])
    except:
        print('fdas')
        break
