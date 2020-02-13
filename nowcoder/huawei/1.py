s = input( )
# l = list(s)
count = 0
for letter in s:
    if letter == ' ':
        count = 0
    else:
        count = count + 1
print(count)
