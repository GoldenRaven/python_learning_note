import math
while True:
    try:
        h = int(input())
        n = 5
        l = [h*math.pow(2, -1*(i-2)) for i in range(2, n+1)]
        # print(l)
        print(round(sum(l)+h, 5))
        print(round(h/math.pow(2,n), 5))
    except:
        break
