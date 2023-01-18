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

marks = [2, 2, 4, 4, 5]
marks[1:3] = [4, 3]
print(marks)

i = int(input())

su = 1

while i != 0:
    su *= i % 10
    i = i/10

print(su)

