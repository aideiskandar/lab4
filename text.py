a = []
a.append(300)
a = map(lambda x: 255 if x > 255 else x, a)

x = [2, 3, 4, 5, 6]
y = list(map(lambda v : v * 5, x))
print(list(a))