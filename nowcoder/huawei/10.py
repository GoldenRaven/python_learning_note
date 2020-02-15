s = input()
# s =  '1`a890-)(*&^%$#@#$%^&*()_P:"}||"?><./'\['
l = list(s)
ls = list(set(l))
ls_filter = [x for x in ls if ( ord(x) > 0 & ord(x) < 128)]
print(len(ls_filter))
