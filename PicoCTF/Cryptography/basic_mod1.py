li = [128, 322, 353, 235, 336, 73, 198, 332, 202, 285, 57, 87, 262, 221, 218, 405, 335, 101, 256, 227, 112, 140 ]

res = [i%37 for i in (li)]

def mapped(res):
    characterset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    ans = ''
    for num in res:
            ans += (characterset[num])
    print(ans)

answer = mapped(res)
