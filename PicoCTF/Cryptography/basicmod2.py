from sympy import mod_inverse
num_str =  '432 331 192 108 180 50 231 188 105 51 364 168 344 195 297 342 292 198 448 62 236 342 63'
li = list(map(int, num_str.split()))

res = [i%41 for i in (li)]
print(res)
mli = []
for i in res:
    inverse = mod_inverse(i,41)
    mli.append(inverse)

print(mli)
def mapped(mli):
    characterset = "aABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    print(len(characterset))
    ans = ''
    for num in mli:
            
            ans += ((characterset[num]))
    print(ans)

answer = mapped(mli)
