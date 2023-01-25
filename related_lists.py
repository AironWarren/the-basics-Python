# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __str__(self):
#         return f"[{self.data}]->{self.next}"


# n = int(input("Введите натуральное число не более 100: "))
#
# if n < 1 or n > 100:
#     print("Число введено не верно")
# else:
#     p = 1
#     for i in range(1, n + 1):
#         p *= i
#
#     print(f"Факториал {n}! = {p}")


# for i in range(1, 7):
#     print('*' * i)


# words = ["Python", "дай", "мне", "силы"]
#
# s = ""
#
# for w in words:
#     # s += w
#     s += ' ' + w
#
# print(s.lstrip())
#
# print(" ".join(words))


# digs = [4, 3, 100, -53, 30, 1, 34, -8]
#
#
# for i, j in enumerate(digs):
#     if 10 < abs(j) < 99:
#         digs[i] = 0
#
# print(digs)


# t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h', 'c',
#      'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']
#
# start_index = ord('а')
# title = "Привет Максим - ваше капец"
# slug = ""
#
# for s in title.lower():
#     if 'а' <= s <= 'я':
#         slug += t[ord(s) - start_index]
#     elif s == 'ё':
#         slug += 'yo'
#     elif s in ' !?;:.,':
#         slug += '-'
#     else:
#         slug += s
#
# while slug.count('--'):
#     slug = slug.replace('--', '-')
#
# print(slug)


# s = input()
#
# i = 0
#
# u = []
#
# for i in range(len(s)-1):
#     if (s[i] + s[i + 1]) == "ра":
#         u.append(i)
#
# if len(u) == 0:
#     print(-1)
# else:
#     print(*u)


# msg = '+7(xxx)xxx-xx-xx'
#
# st = input()
# sm = 0
# i = 0
#
# if len(msg) == len(st):
#     for i, j in enumerate(st):
#         if (msg[i] == j) or (j.isdigit() and msg[i] == "x"):
#             sm += 0
#         else:
#             sm += 1
# else:
#     sm = 1
#
# if sm == 0:
#     print('ДА')
# else:
#     print('НЕТ')

# n = input()
# n = n.replace(' ', '')
# n = n.replace('+', '_+')
# n = n.replace('-', '_-')
# k = list(map(int, n.split('_')))
# print(sum(k))


# n = int(input())
#
# z = []
# m = []
#
# for a in range(n):
#     z.append(list())
#
#
# for i in range(n):
#     for j in range(n):
#         if j == n - 1:
#             z[i].append(5)
#         else:
#             z[i].append(1)
#     m.append(z[i])
#     print(*m[i])

# Алгоритм сортировки выбором
# n = list(map(int, input().split()))
#
# s = 0
# t = 0
# q = 0
#
# for i in range(0, len(n) - 1):
#     s = n[i]
#     q = i
#     for j in range(i + 1, len(n)):
#         if s > n[j]:
#             s = n[j]
#             q = j
#
#     if q != i:
#         t = n[i]
#         n[i] = n[q]
#         n[q] = t
#
#
# print(n)

# Треугольник Паскаля

# n = int(input())
#
# p = []
#
# for i in range(n):
#     row = [1] * (i + 1)
#     for j in range(i + 1):
#         if j != 0 and j != i:
#             row[j] = p[i-1][j-1] + p[i-1][j]
#
#     p.append(row)
#
# for r in p:
#     print(*r)
