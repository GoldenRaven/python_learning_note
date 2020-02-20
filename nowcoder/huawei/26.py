while True:
    try:
        n = int(input())
        a, b = 1, 1
        if n < 3:
            print(1)
        else:
            for i in range(3, n+1):
                c = a+b
                a, b = b, c
            print(c)
    except:
        break
