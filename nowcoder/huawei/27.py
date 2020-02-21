import math
while True:
    try:
        h = int(input())
        n = 5
        print(sum([h, h, h/2.0, h/4.0, h/8.0]))
        print(h/math.pow(2,5))
    except:
        break
