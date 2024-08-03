import random
n = 6
m = 4
s = n + m
N = 10 ** 7
f = 0
for a in range(1, N + 1):
    k = 0
    l = []
    for x in range(1, n + 1):
        l.append(5)
    for y in range(1, m + 1):
        l.append(10)
    random.shuffle(l)
    c = []
    for z in l:
        if z == 5:
            k += 1
            c.append(z)
        else:
            c.append(z)
            if 5 in c:
                k += 1
                c.remove(5)
            else:
                break
        if k == s:
            f += 1

print("Вероятность путём моделирования =", f / N)
print("Вероятность путём аналитики =", (n - m + 1) / (n + 1))
