import random

k = 0 # счётчик А
N = 10**7

for z in range(1, N + 1):
    x = random.uniform(0.0, 12.0)
    y = random.uniform(0.0, 4.0)
    a = [0, 4, 8, 12]
    b = [y, y + 6]
    v = 0
    w = 0
    for i in a:
        if x > i:
            continue
        else:
            v = i
            break
    for j in b:
        if x > j:
            if x > b[1]:
                w = 100
        else:
            w = j
            break
    if v < w:
        k += 1

print("Вероятность путём моделирования =", round(k / N, 5))
print("Вероятность путём аналитики =", round(2 / 3, 5))
