import random

p1 = 0.4
p2 = 0.9
p3 = 0.1
q1 = 1 - p1
q2 = 1 - p2
q3 = 1 - p3

N = 10**7  # количество выходов из B1
k = 0

for i in range(1, N +1):
    x = random.choices([2, 3], weights=[p1, q1]) # в B2 или в B3
    x = x[0]
    if x == 2: # попадаем в B2 (p1)
        x = random.choices([3, 4], weights=[p2, q2]) # в B3 или в B4
        x = x[0]
        if x == 3: # попадаем в B3 (p2)
            x = random.choices([2, 4], weights=[q3, p3]) # в B2 или в B4
            x = x[0]
            if x == 2: # попадаем в B2 (q3)
                x = random.choices([3, 4], weights=[p2, q2]) # в B3 или в B4
                x = x[0]
                if x == 3: # попадаем в B3 (p2)
                    x = random.choices([2, 4], weights=[q3, p3]) # в B3 или в B4
                    x = x[0]
                else: # попадаем в B4 (q2)
                    k += 1
            else: # попадаем в B4 (p3)
                k += 1
        else: # попадаем в B4 (q2)
            k += 1
    else: # попадаем в B3 (q1)
        x = random.choices([2, 4], weights=[q3, p3]) # в B2 или в B4
        x = x[0]
        if x == 2: # попадаем в B2 (q3)
            x = random.choices([3, 4], weights=[p2, q2]) # в B3 или в B4
            x = x[0]
            if x == 3: # попадаем в B3 (p2)
                x = random.choices([2, 4], weights=[q3, p3]) # в B2 или в B4
                x = x[0]
                if x == 2: # попадаем в B2 (q3)
                    x = random.choices([3, 4], weights=[p2, q2]) # в B3 или в B4
                    x = x[0]
                else: # попадаем в B4 (p3)
                    k += 1
            else: # попадаем в B4 (q2)
                k += 1
        else: # попадаем в B4 (p3)
            k += 1

res = p2 * q3 * (p1 * p2 + q1 * q3)
print("Вероятность путём аналитики =", 1 - res)
print("Вероятность путём моделирования =", round(k / N, N))
