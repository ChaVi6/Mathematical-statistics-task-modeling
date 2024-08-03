import random

k = 0 # счётчик А
N = 1

for z in range(1, N + 1):
    y = 0
    for x in range(0, 13):
        print("№", x)
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

        print("A =", v)
        print("B =", w)
        print("k =", k)
        print("Интервал между автобусом А и следующим автобусом B:", y, "минут(ы)")
        print("Расписание автобусов линии А:", a)
        print("Расписание автобусов линии B:", b)
        print("Момент прихода пассажира:", x, "минута\n")

print("P =", k / N)
