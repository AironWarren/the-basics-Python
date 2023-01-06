import math

math.f

s = 'python'

S = s.upper()

m = S.lower()

c = s.count('p')

msg = 'abrakadabra'

print(S)
print(m)
print(c)

d = 'abc'

print(msg.rfind('bra'))

print(msg.replace('a', 'o', 2))

print(d.rjust(5, '0'))

digs = '1, 2,3,  4,5, 6'

print(digs.replace(' ', '').split(','))

b = digs.replace(' ', '').split(',')

print(' '.join(b))

fio = 'Иванов Иван Иванович'

print(fio.replace(' ', ', '))
print(', '.join(fio.split()))
