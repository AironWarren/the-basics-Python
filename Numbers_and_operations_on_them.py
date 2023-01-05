import math
m = input()
b = 7
c = 45.3

print(m, b, c, sep=" | ", end=" ")

print(f"x = {b}; y = {c}")

a, b = map(float, input("Введите стороны прямоугольника: ").split())

print(type(a))
print(f"Периметр: = {2 * (a + b)}")

