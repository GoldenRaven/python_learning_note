s = 'asdf234GDSdsf23'
def key1(y):
    yy = (y.isdigit(),y.isdigit() and int(y) % 2 == 0,y.isupper(),y)
    print(yy)
    return yy
ss = sorted(s, key=key1)
print(ss)

# exit(0)
#input: 'asdf234GDSdsf23'

# print(sorted([[2, 1, 0, 1, 0],[0, 1, 0, 1, 0],[1, 1, 0, 0]]))
# exit(0)
# my_alphabet = ['a', 'b', 'c']

# def custom_key(word):
#    numbers = []
#    for letter in word:
#       numbers.append(my_alphabet.index(letter))
#    print(sum(numbers))
#    return sum(numbers)
# # python中的整数列表能够比较大小
# # custom_key('cbaba')==[2, 1, 0, 1, 0]

# x=['cbaba', 'ababa', 'bbaa']
# x.sort(key=custom_key)
# print(x)
