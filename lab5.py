#F(0) = F(1) = 10, F(n) = F(n–2)! – 2*F(n-1), при n > 1


import time
from matplotlib import pyplot
from scipy.special import factorial

n = int(input("Введите число n: "))

def Recursive(n):
    if n <= 1:
        return 10
    else:
        return factorial(Recursive(n-2)) - 2 * Recursive(n-1)


def Iteratively(n):
    if n <= 1:
        return 10
    else:
        zer, one = 10, 10
        for i in range(2, n + 1):
            res = factorial(zer) - 2 * one
            zer, one = one, res
        return res


startr = time.time()
rec = Recursive(n)
endr = time.time()
timer = endr - startr
print("Рекурсивно при n = {} F(n) = {}, решено за {:.2f} секунд)".format(n, rec, timer))

starti = time.time()
ite = Iteratively(n)
endi = time.time()
timei = endi - starti
print("Итерационно при n = {} F(n) = {}, решено за {:.2f} секунд)".format(n, ite, timei))

pyplot.ylabel('n')
pyplot.xlabel('Время (в сек.)')
pyplot.plot([timer], [n], 'ro', label='Рекурсивно')
pyplot.plot([timei], [n], 'go', label='Итеративно')
pyplot.legend()
pyplot.show()
