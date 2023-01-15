x = -4
if x < 0:
    x = -x
print(x)

# a = float(input())

# if 4 <= a <= 10:
#     print("a в диапазон входит")
# else:
#     print("a в диапазон не входит")

print(7.5 % 10)


# крутая задача
# put your python code here
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m, n = map(int, input().split())

if n == 1:
    n1 = month[m-2]
    n2 = n + 1
    m1 = m - 1
    m2 = m
elif n == month[m - 1]:
    n1 = n - 1
    m1 = m
    n2 = 1
    m2 = m + 1
else:
    n1 = n - 1
    n2 = n + 1
    m1 = m
    m2 = m

print(f"{str(m1).rjust(2, '0')}.{str(n1).rjust(2, '0')} {str(m2).rjust(2, '0')}.{str(n2).rjust(2, '0')}")

a = 12
b = 8

res = a + 2 if a > b else b - 5

res = abs(a + 2) if a > b else abs(b - 5)
print(res)

s = 'python'
t = 'upper'
res = s.upper() if t == 'upper' else s
print(res)

a = 12
b = 7

m = [1, 2, a if a < b else b, 6]

print("a -" + ("четное" if a % 2 == 0 else "нечетное") + "число")
