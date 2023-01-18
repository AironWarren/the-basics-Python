i = 0

while i < 10:
    i += 1
    if i == 5:
        break


print(i)




st = list(input().lower().split())

s1 = ''
s2 = ''

s3 = ''
s4 = ''

for i in range(len(st)):
    if i == 0:
        s1 = st[i][0]
        s2 = st[i][-1]
        if s2 in 'ьъы':
            s2 = st[i][-1]
    elif i == len(st) - 1:
        s1 = st[i][0]

        if s1 == s2:
            s2 = st[i][-1]
            if s2 in 'ьъы':
                s2 = st[i][-2]
        else:
            print("НЕТ")
            break
    else:
        s1 = st[i][0]

        if s1 == s2:
            s2 = st[i][-1]
            if s2 in 'ьъы':
                s2 = st[i][-2]
        else:
            print("НЕТ")
            break
else:
    print("ДА")