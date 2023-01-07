a = ['Moscow', 'Novosibirsk', 'Tomsk']

mark = [1, 2, 3, 4, 5]
mark[3] = 10

print(a[1], mark[3])
print(mark)

mes = [1, 'first', True, 5.3, [1, 2, 3]]

# a = []
# b = list('python')
c = list(mes)
d = list([True, False])

# print(a, b, c, d)

print(len(mes[4]), mes[4][1])

print(max(mark), min(mark))

# D = sorted(mes)
# print(D)
f = [1, 2, 3] + [4, 5]
print(f)

print(0 in mes)

del mes[1]
print(mes)

nums = [3, 3]
target = 6
a = 0
b = 0
for item in nums:
    for item2 in nums[(nums.index(item) + 1):]:
        if (item + item2) == target:
            a = item
            b = item2
            break
    if (a + b) == target:
        break
if a == b:
    ans = [nums.index(a), nums.index(b, 1)]
else:
    ans = [nums.index(a), nums.index(b)]
print(f'[{ans[0]},{ans[1]}]')
