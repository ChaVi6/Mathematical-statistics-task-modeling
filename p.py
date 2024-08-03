import random

k = 0 # счётчик А
N = 10**5

for z in range(1, N + 1):
    x = random.randint(0, 12)
    y = random.randint(0, 4)
    a = [0, 4, 8, 12]
    b = [y, y + 6]
    v = 0
    w = 0
    if x == 12:
        x = 0
    for i in a:
        if x >= i:
            continue
        else:
            v = i
            break
    for j in b:
        if x >= j:
            if x > b[1]:
                w = 100
        else:
            w = j
            break
    if x >= b[1]:
        w = b[1] + 6
    if (v - x <= 2) or (w - x <= 2):
        k += 1



print("P =", k / N)
