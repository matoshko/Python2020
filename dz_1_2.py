import numpy

j = (4.2, 0.3, 1.7)
r = 4 * (10 ** (-4))
c = 2.1
m = 7
for i in range(len(j)):
    h = (10 * r - j[i]) / (c ** 2 + numpy.e ** (-m))
    y = (h * m - j[i] ** 2) + (0.1 *c) ** 2
    print(y)

j = 0
while j <= 1.7:
    h = (10 * r - j) / (c ** 2 + numpy.e ** (-m))
    a = (h * m - j ** 2) + (0.1*c) ** 2
    j += 0.5
    print(a)

j = (9, 1.8, 15, -3)
m = 1
for n in range(len(j)):
    while m <= 2:
        h = (10 * r - j[n]) / (c ** 2 + numpy.e ** (-m))
        b = (h * m - j[n] ** 2) + (0.1*c) ** 2
        m += 0.5
        print(b)