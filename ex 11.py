import random
N = 10**5
j = 0
for a in range(N):
    mass = []
    k = 0
    particles = random.randint(1, 10) # генерация кол-ва частиц
    for i in range(particles):
        mass.append(random.choices(['A', 'B', 'C', 'OUT'], weights=[0.1, 0.2, 0.2, 0.5])) # вероятность попадания
    if ['A'] in mass:
        k += 1
    if (['B'] in mass) and (['C'] in mass):
        k += 1
    if k >= 1:
        j += particles

print("Вероятность путём моделирования =", j/N)
print("Вероятность путём аналитики (из учебника) =", 14/3)