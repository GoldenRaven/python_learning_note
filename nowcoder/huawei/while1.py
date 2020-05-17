def sumtree(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            # items.extend(front)
            items[:0] = front
    return tot

l = [4,[2,9],[23,345,[3456,987],[[123,456,7],98],987]]
print(sumtree(l))
